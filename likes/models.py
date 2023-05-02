from django.db import models


class Like(models.Model):
    liked_by = models.ForeignKey("users.User", on_delete=models.CASCADE)
    post = models.ForeignKey(
        "posts.Post", related_name="likes", on_delete=models.CASCADE
    )
    liked_at = models.DateTimeField(auto_now_add=True)
