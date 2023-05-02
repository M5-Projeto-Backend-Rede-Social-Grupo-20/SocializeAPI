from django.db import models


class Comment(models.Model):
    comment = models.CharField(max_length=225)
    commented_by = models.ForeignKey("users.User", on_delete=models.CASCADE)
    commented_at = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(
        "posts.Post", on_delete=models.CASCADE, related_name="comments"
    )
