from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    email = models.EmailField(max_length=120, unique=True)
    birth_date = models.DateField(max_length=12, null=True, blank=True)
