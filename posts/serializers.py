from rest_framework import serializers

from users.serializers import ShortUserSerializer
from .models import Post, AccessChoices, Like, Comment
from django.forms.models import model_to_dict


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


class PostSerializer(serializers.ModelSerializer):
    access = serializers.ChoiceField(choices=AccessChoices.choices)
    posted_by = ShortUserSerializer(read_only=True)

    class Meta:
        model = Post
        fields = (
            "id",
            "posted_by",
            "content",
            "access",
            "created_at",
        )
        read_only_fields = ("id", "created_at", "posted_by", "comments", "likes")
