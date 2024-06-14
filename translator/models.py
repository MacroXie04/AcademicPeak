from django.db import models

class Translation(models.Model):
    session = models.IntegerField()
    text = models.TextField()
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.session