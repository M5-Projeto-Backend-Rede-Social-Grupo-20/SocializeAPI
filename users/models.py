from django.db import models
from django.contrib.auth.models import AbstractUser


# class User(AbstractUser):
#     connections = models.ForeignKey(
#         "connections.Connection", related_name="received_by", on_delete=models.CASCADE
#     )


class User(AbstractUser):
    connection = models.ForeignKey(
        "connections.Connection",
        related_name="user",
        on_delete=models.CASCADE,
        null=True,
    )
