from django.db import models


class University(models.Model):
    """University model"""
    # Rank information, auto generate by database
    rank = models.IntegerField()

    # name and country information
    name = models.CharField(max_length=50)
    country = models.CharField(max_length=30)

    # introduction of university
    info = models.TextField()
    tuition = models.IntegerField()
    website_link = models.URLField()

    # university photo
    photo_url = models.URLField(blank=True)
    photo = models.ImageField(upload_to='university/static/photo/', blank=True)

    def __str__(self):
        return self.name
