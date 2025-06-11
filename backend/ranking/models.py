# app/models.py
"""
Django ORM models for a HugerScore‑style rating system.

Entities
--------
Category  : A top‑level category (e.g., Tech, Movies, Sports).
Tag       : A free‑form label for flexible filtering.
Item      : Anything that can be rated (phone, film, player, etc.).
Rating    : A single user’s 1–5‑star rating (with optional short review).
"""
from django.db import models
from django.contrib.auth import get_user_model
from django.db.models import Avg, Count

User = get_user_model()


class TimeStampedModel(models.Model):
    """Abstract base model that adds `created_at` and `updated_at`."""
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Category(TimeStampedModel):
    """Top‑level category (e.g., Tech, Movies, Sports)."""
    name = models.CharField(max_length=64, unique=True)
    slug = models.SlugField(max_length=64, unique=True)
    description = models.TextField(blank=True)

    class Meta:
        db_table = "rating_category"
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self) -> str:  # pragma: no cover
        return self.name


class Tag(TimeStampedModel):
    """Free‑form label for extra filtering (e.g., ‘5G’, ‘OLED’, ‘Oscar’)."""
    name = models.CharField(max_length=32, unique=True)
    slug = models.SlugField(max_length=32, unique=True)

    class Meta:
        db_table = "rating_tag"
        verbose_name = "Tag"
        verbose_name_plural = "Tags"

    def __str__(self) -> str:  # pragma: no cover
        return self.name


class Item(TimeStampedModel):
    """
    An entity that receives ratings.

    Cached fields
    -------------
    avg_score   : Average of all related ratings (1.00–5.00, 2‑decimal).
    score_count : Total number of ratings.
    """
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    description = models.TextField(blank=True)
    category = models.ForeignKey(
        Category, related_name="items", on_delete=models.CASCADE
    )
    creator = models.ForeignKey(
        User,
        related_name="created_items",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )
    cover = models.ImageField(upload_to="rating_covers/", null=True, blank=True)

    # cached statistics
    avg_score = models.DecimalField(max_digits=4, decimal_places=2, default=0)
    score_count = models.PositiveIntegerField(default=0)

    tags = models.ManyToManyField(Tag, related_name="items", blank=True)

    class Meta:
        db_table = "rating_item"
        verbose_name = "Item"
        verbose_name_plural = "Items"
        indexes = [
            models.Index(fields=["avg_score"]),
            models.Index(fields=["score_count"]),
        ]

    # --------------------------------------------------------------------- #
    # Business helpers                                                      #
    # --------------------------------------------------------------------- #
    def __str__(self) -> str:  # pragma: no cover
        return self.title

    def refresh_score(self, commit: bool = True) -> None:
        """
        Recalculate and cache `avg_score` and `score_count`.

        Heavy‑traffic sites should run this asynchronously (e.g., Celery) or
        update incremental counters instead of full aggregation.
        """
        agg = self.ratings.aggregate(avg=Avg("stars"), cnt=Count("id"))
        self.avg_score = round(agg["avg"] or 0, 2)
        self.score_count = agg["cnt"]
        if commit:
            self.save(update_fields=["avg_score", "score_count"])

    @property
    def score_10_scale(self) -> float:
        """Return the score converted to a 10‑point scale (for display)."""
        return float(self.avg_score) * 2


class Rating(TimeStampedModel):
    """A single user’s star rating (1–5) plus optional short review."""
    STAR_CHOICES = [(i, f"{i} Star") for i in range(1, 6)]

    item = models.ForeignKey(
        Item, related_name="ratings", on_delete=models.CASCADE
    )
    user = models.ForeignKey(
        User, related_name="ratings", on_delete=models.CASCADE
    )
    stars = models.PositiveSmallIntegerField(choices=STAR_CHOICES)
    review = models.TextField(blank=True)

    class Meta:
        db_table = "rating_rating"
        verbose_name = "Rating"
        verbose_name_plural = "Ratings"
        unique_together = ("item", "user")           # one rating per user/item
        indexes = [
            models.Index(fields=["item", "stars"]),
            models.Index(fields=["user"]),
        ]

    def __str__(self) -> str:  # pragma: no cover
        return f"{self.user} → {self.item}: {self.stars}★"

    # --------------------------------------------------------------------- #
    # Hooks                                                                 #
    # --------------------------------------------------------------------- #
    def save(self, *args, **kwargs):
        """
        Save the rating and immediately refresh the parent item’s cache.

        For performance you may restrict cache updates to new ratings only,
        or debounce with a background job.
        """
        super().save(*args, **kwargs)
        self.item.refresh_score(commit=True)