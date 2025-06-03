import os
import uuid
from django.contrib.auth.models import User
from django.db import models


# Generate a unique file path for user uploads
def user_directory_path(instance, filename):
    ext = filename.split('.')[-1]
    unique_filename = f"{instance.user.username}_{uuid.uuid4().hex}.{ext}"
    return os.path.join('avatars', unique_filename)


class UserProfile(models.Model):
    # foreign key link the user model
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)

    # user profile fields
    gender = models.CharField(blank=True, null=True)
    profile_img = models.ImageField(upload_to=user_directory_path, blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Profile of {self.user.username}"
