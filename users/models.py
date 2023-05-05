from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid


class GENDER(models.TextChoices):
    M = "Male"
    F = "Female"
    N = "Not Informed"


class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    email = models.CharField(max_length=255, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birthdate = models.DateField(null=True)
    bio = models.TextField(null=True)
    gender = models.CharField(
        max_length=20, choices=GENDER.choices, default="Not Informed"
    )
    city = models.CharField(max_length=100, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
