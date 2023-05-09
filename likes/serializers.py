from rest_framework import serializers

from users.serializers import ShortUserSerializer
from posts.serializers import ShortPostSerializer
from .models import Like


class LikeSerializer(serializers.ModelSerializer):
    liked_by = ShortUserSerializer(read_only=True)
    post = ShortPostSerializer(read_only=True)

    class Meta:
        model = Like
        fields = (
            "id",
            "liked_by",
            "post",
            "created_at",
        )
