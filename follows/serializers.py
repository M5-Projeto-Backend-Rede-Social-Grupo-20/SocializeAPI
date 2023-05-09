from rest_framework import serializers
from django.shortcuts import get_object_or_404

from .models import Follow
from users.serializers import UserSerializer


class FollowCreateSerializer(serializers.ModelSerializer):
    from_user = UserSerializer(read_only=True)
    to_user = UserSerializer(read_only=True)

    class Meta:
        model = Follow
        fields = ["id", "from_user", "to_user", "created_at"]
        read_only_fields = ["id", "created_at"]

    def create(self, validated_data):
        from_user = validated_data["from_user"]
        to_user = validated_data["to_user"]

        if from_user == to_user:
            raise serializers.ValidationError("You cannot follow yourself.")

        follow = to_user.followers.filter(from_user=from_user).first()
        if follow:
            raise serializers.ValidationError("You already followed this user.")

        return Follow.objects.create(**validated_data)


class FollowersListSerializer(serializers.ModelSerializer):
    follower = UserSerializer(read_only=True, source="from_user")

    class Meta:
        model = Follow
        fields = ["id", "follower", "created_at"]
        read_only_fields = ["id", "created_at"]


class FollowingListSerializer(serializers.ModelSerializer):
    following = UserSerializer(read_only=True, source="to_user")

    class Meta:
        model = Follow
        fields = ["id", "following", "created_at"]
        read_only_fields = ["id", "created_at"]
