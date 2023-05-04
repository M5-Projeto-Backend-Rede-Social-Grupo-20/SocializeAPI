from django.db import models
import uuid


class Friendship(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    from_user = models.ForeignKey(
        "users.user", related_name="friendship_sent", on_delete=models.CASCADE
    )
    to_user = models.ForeignKey(
        "users.user",
        related_name="friendship_received",
        on_delete=models.CASCADE,
    )

    is_accepted = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
