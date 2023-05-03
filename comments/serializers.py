from rest_framework import serializers
from .models import Comment
from users.serializers import UserSerializer


class CommentSerializer(serializers.ModelSerializer):
    commented_by = UserSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = [
            'id',
            'comment',
            'commented_by',
            'commented_at',
            'post',
        ]
        read_only_fields = [
            'id',
            'commented_by',
            'commented_at',
            'post',
        ]

