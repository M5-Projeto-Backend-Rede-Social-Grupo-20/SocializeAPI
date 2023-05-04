from django.db import models


class Connection(models.Model):
    from_user = models.ForeignKey(
        "users.User", related_name="following", on_delete=models.CASCADE
    )
    to_user = models.ForeignKey(
        "users.User", related_name="followers", on_delete=models.CASCADE
    )
    is_friend = models.BooleanField(default=False)
    is_following = models.BooleanField(default=False)
    friend_accepted = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)
