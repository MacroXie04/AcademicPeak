import os
import uuid
from django.contrib.auth.models import User
from django.db import models


# Generate a unique file path for user uploads
def user_directory_path(instance, filename):
    ext = filename.split('.')[-1]
    unique_filename = f"{instance.user.username}_{uuid.uuid4().hex}.{ext}"
    return os.path.join('avatars', unique_filename)


class TimeStampedModel(models.Model):
    """Abstract base model that adds `created_at` and `updated_at`."""
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class UserProfile(TimeStampedModel):
    # foreign key link the user model
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)

    # user profile fields
    gender = models.CharField(max_length=20, blank=True, null=True)
    profile_img = models.ImageField(upload_to=user_directory_path, blank=True, null=True)

    def __str__(self):
        return f"Profile of {self.user.username}"


class WebAuthnCredential(TimeStampedModel):
    """
    Stores WebAuthn credential information for a user.

    This model is used to store the necessary information for WebAuthn
    authentication, including the credential ID, public key, and sign count.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='webauthn_credentials')
    credential_id = models.CharField(max_length=255, unique=True)
    public_key = models.TextField()
    sign_count = models.PositiveIntegerField(default=0)

    # Additional fields that might be useful
    credential_name = models.CharField(max_length=100, blank=True, null=True)  # User-friendly name for the credential
    last_used_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        verbose_name = "WebAuthn Credential"
        verbose_name_plural = "WebAuthn Credentials"

    def __str__(self):
        return f"WebAuthn Credential for {self.user.username}"
