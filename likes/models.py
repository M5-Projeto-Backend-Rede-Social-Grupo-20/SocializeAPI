from django.db import models
import uuid


class Like(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    liked_by = models.ForeignKey(
        "users.user", related_name="likes", on_delete=models.CASCADE
    )
    post = models.ForeignKey(
        "posts.post", related_name="likes", on_delete=models.CASCADE
    )

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("-created_at",)
