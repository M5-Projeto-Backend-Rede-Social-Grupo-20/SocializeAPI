from rest_framework import serializers

from users.serializers import ShortUserSerializer
from .models import Post, AccessChoices


class ShortPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = (
            "id",
            "posted_by",
            "content",
            "access",
        )
        read_only_fields = ("id", "created_at", "posted_by", "comments", "likes")


class PostSerializer(serializers.ModelSerializer):
    access = serializers.ChoiceField(choices=AccessChoices.choices)
    posted_by = ShortUserSerializer(read_only=True)
    likes_count = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = (
            "id",
            "posted_by",
            "content",
            "access",
            "created_at",
            "likes_count",
        )
        read_only_fields = ("id", "created_at", "posted_by", "comments", "likes")

    def get_likes_count(self, obj):
        return obj.likes.count()
