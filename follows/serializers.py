from rest_framework import serializers
from django.shortcuts import get_object_or_404

from .models import Follow
from users.models import User
from users.serializers import UserSerializer


class FollowSerializer(serializers.ModelSerializer):
    from_user = UserSerializer(read_only=True)
    to_user = UserSerializer(read_only=True)

    class Meta:
        model = Follow
        fields = ["id", "from_user", "to_user", "created_at"]
        read_only_fields = ["id", "created_at"]

    def create(self, validated_data):
        if validated_data["from_user"] == validated_data["to_user"]:
            raise serializers.ValidationError("You cannot follow yourself.")
        follow = Follow.objects.filter(
            from_user=validated_data["from_user"], to_user=validated_data["to_user"]
        ).first()
        if follow:
            raise serializers.ValidationError("You already followed this user.")
        return Follow.objects.create(**validated_data)
