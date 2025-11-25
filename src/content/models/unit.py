from django.db import models
from .subject import Subject

class Unit(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name="units")
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True, default="")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        app_label = 'content'

    def __str__(self):
        return self.title

