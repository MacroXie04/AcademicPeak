from django.db import models

# Create your models here.

class Markdown(models.Model):
    subject = models.CharField(max_length=100)
    item = models.CharField(max_length=100)
    uploaded = models.DateTimeField(auto_now_add=True)
    content = models.TextField()

    def __str__(self):
        return f'{self.subject}{self.item}'