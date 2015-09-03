from django.db import models
from django.contrib.auth.models import AbstractUser

class MyUser(AbstractUser):
    designation = models.CharField(max_length=200)


# Create your models here.
