from rest_framework import serializers

from users.serializers import UserSerializer
from .models import Post, AccessChoices, Like, Comment


class PostSerializer(serializers.ModelSerializer):
    access = serializers.ChoiceField(choices=AccessChoices.choices)
    posted_by = UserSerializer(read_only=True)

    class Meta:
        model = Post
        fields = (
            "id",
            "posted_by",
            "content",
            "access",
            "created_at",
            "comments",
            "likes",
        )
        read_only_fields = ("id", "created_at", "posted_by", "comments", "likes")

class LikeSerializer(serializers.ModelSerializer):
    liked_by = UserSerializer(read_only=True)
    posted_in = PostSerializer(read_only=True)

    class Meta:
        model = Like
        fields = ('id', 'liked_by', 'posted_in', 'created_at',)


class CommentSerializer(serializers.ModelSerializer):
    commented_by = UserSerializer(read_only=True)
    posted_in = PostSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = [
            'id',
            'content',
            'commented_by',
            'posted_in',
            'created_at',
        ]
        read_only_fields = [
            'id',
            'commented_by',
            'created_at',
            'posted_in',
        ]



