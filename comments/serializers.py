from rest_framework import serializers

from .models import Comment
from users.serializers import ShortUserSerializer
from posts.serializers import ShortPostSerializer


class CommentSerializer(serializers.ModelSerializer):
    commented_by = ShortUserSerializer(read_only=True)
    post = ShortPostSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = [
            "id",
            "content",
            "commented_by",
            "post",
            "created_at",
        ]
        read_only_fields = [
            "id",
            "commented_by",
            "created_at",
            "post",
        ]
