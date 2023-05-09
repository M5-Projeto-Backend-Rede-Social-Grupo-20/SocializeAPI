from django.db import models
import uuid


class Follow(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    from_user = models.ForeignKey(
        "users.user", related_name="following", on_delete=models.CASCADE
    )
    to_user = models.ForeignKey(
        "users.user", related_name="followers", on_delete=models.CASCADE
    )

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("-created_at",)
