from django.db import models

# Create your models here.

class Person(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    birthday = models.DateField()
    email = models.EmailField()
    phone = models.CharField(max_length=15)
