from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """
    Custom User model extending Django's AbstractUser.

    This allows for future customization without difficult migrations.
    Add custom fields here as needed.
    """
    # Example custom fields (uncomment and modify as needed):
    # bio = models.TextField(max_length=500, blank=True)
    # profile_picture = models.ImageField(upload_to='profiles/', null=True, blank=True)
    # phone_number = models.CharField(max_length=20, blank=True)

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return self.username
