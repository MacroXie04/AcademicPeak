from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name

class Item(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='items/')
    description = models.TextField()
    overall_score = models.FloatField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def update_score(self):
        scores = self.scores.all()
        if scores.exists():
            self.overall_score = sum(score.value for score in scores) / scores.count()
        else:
            self.overall_score = 0.0
        self.save()

    def __str__(self):
        return self.name

class Score(models.Model):
    item = models.ForeignKey(Item, related_name='scores', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    value = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

    # for safe and fare score
    browser_fingerprint = models.CharField(max_length=255)
    ipaddress = models.CharField(max_length=45)

    def __str__(self):
        return f'{self.value} by {self.user} on {self.item}'


