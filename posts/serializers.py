from rest_framework import serializers
from .models import Post, AccessChoices
from users.serializers import UserSerializer


class PostSerializer(serializers.ModelSerializer):
    access = serializers.ChoiceField(choices=AccessChoices.choices)
    posted_by = UserSerializer(read_only=True)

    class Meta:
        model = Post
        fields = (
            "id",
            "access",
            "text",
            "created_at",
            "posted_by",
            "comments",
            "likes",
        )
        read_only_fields = ("id", "created_at", "posted_by", "comments", "likes")
