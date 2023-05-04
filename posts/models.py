from django.db import models


class AccessChoices(models.TextChoices):
    PRIVATE = "private"
    PUBLIC = "public"


class Post(models.Model):
    access = models.CharField(
        choices=AccessChoices.choices, max_length=7, default=AccessChoices.PUBLIC
    )
    text = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    posted_by = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="posts"
    )
