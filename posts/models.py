from django.db import models
import uuid


class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    user = models.ForeignKey(
        "users.user", related_name="posts", on_delete=models.CASCADE
    )

    content = models.TextField()
    is_public = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)


class Comment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    user = models.ForeignKey(
        "users.user", related_name="comments", on_delete=models.CASCADE
    )
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)

    content = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)


class Like(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    user = models.ForeignKey(
        "users.user", related_name="likes", on_delete=models.CASCADE
    )
    post = models.ForeignKey(Post, related_name="likes", on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
