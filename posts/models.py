from django.db import models
import uuid


class AccessChoices(models.TextChoices):
    PRIVATE = "private"
    PUBLIC = "public"


class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    posted_by = models.ForeignKey(
        "users.user", related_name="posts", on_delete=models.CASCADE
    )

    content = models.TextField()
    access = models.CharField(
        choices=AccessChoices.choices, max_length=7, default=AccessChoices.PUBLIC
    )

    created_at = models.DateTimeField(auto_now_add=True)


class Comment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    content = models.TextField()

    commented_by = models.ForeignKey(
        "users.user", related_name="comments", on_delete=models.CASCADE
    )
    posted_in = models.ForeignKey(
        Post, related_name="comments", on_delete=models.CASCADE
    )

    created_at = models.DateTimeField(auto_now_add=True)


class Like(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    liked_by = models.ForeignKey(
        "users.user", related_name="likes", on_delete=models.CASCADE
    )
    post = models.ForeignKey(Post, related_name="likes", on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
