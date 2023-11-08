from django.db import models
from django.contrib.auth.models import User
import markdown2
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


class University(models.Model):
    university_rank = models.IntegerField()
    university_name = models.CharField(max_length=30)
    university_country = models.CharField(max_length=30)
    university_global_score = models.IntegerField()
    university_enrollment = models.IntegerField()
    university_link = models.CharField(max_length=100)
    university_photo_link = models.CharField(max_length=100)
