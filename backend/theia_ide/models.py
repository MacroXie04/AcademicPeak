from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class TimeStampedModel(models.Model):
    """Abstract base model that adds `created_at` and `updated_at`."""
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class IDEInstance(TimeStampedModel):
    """
    Represents a Theia IDE instance associated with a user.

    This model stores information about the IDE environment, including
    its configuration, current status, and access URL.
    """
    STATUS_CHOICES = [
        ('creating', 'Creating'),
        ('running', 'Running'),
        ('stopped', 'Stopped'),
        ('error', 'Error'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ide_instances')
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    # Environment configuration
    environment_type = models.CharField(max_length=50, default='python')  # e.g., python, java, node
    environment_version = models.CharField(max_length=20, default='3.9')  # e.g., 3.9, 17, 16
    memory_limit_mb = models.PositiveIntegerField(default=512)
    cpu_limit = models.DecimalField(max_digits=3, decimal_places=1, default=1.0)

    # Instance status
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='creating')
    access_url = models.URLField(blank=True, null=True)
    container_id = models.CharField(max_length=100, blank=True, null=True)

    # Usage tracking
    last_accessed_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        verbose_name = "IDE Instance"
        verbose_name_plural = "IDE Instances"

    def __str__(self):
        return f"{self.name} ({self.environment_type}) - {self.status}"
