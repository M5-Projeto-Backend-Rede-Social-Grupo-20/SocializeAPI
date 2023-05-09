from django.db import models
import uuid


class Comment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    content = models.TextField()

    commented_by = models.ForeignKey(
        "users.user", related_name="comments", on_delete=models.CASCADE
    )
    post = models.ForeignKey(
        "posts.post", related_name="comments", on_delete=models.CASCADE
    )

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("-created_at",)
