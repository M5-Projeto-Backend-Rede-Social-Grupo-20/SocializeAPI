from rest_framework import serializers
from .models import Like
from users.serializers import UserSerializer
from posts.serializers import PostSerializer


class LikeSerializer(serializers.ModelSerializer):
    liked_by = UserSerializer(read_only=True)
    post = PostSerializer(read_only=True)

    class Meta:
        model = Like
        fields = ('id', 'liked_by', 'post', 'liked_at',)
