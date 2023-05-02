from django.db import models


# class Connection(models.Model):
#     following = models.BooleanField(default=False)
#     friend = models.BooleanField(default=False)
#     is_accepted = models.BooleanField(default=False)
#     requested_by = models.ForeignKey("users.User", on_delete=models.CASCADE)


class Connection(models.Model):
    following = models.BooleanField(default=False)
    friend = models.BooleanField(default=False)
    is_accepted = models.BooleanField(default=False)
    requested_by = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="connections"
    )
