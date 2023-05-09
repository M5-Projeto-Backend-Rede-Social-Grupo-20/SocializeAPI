from rest_framework import serializers

from .models import Friendship
from users.serializers import UserSerializer


class FriendshipListSerializer(serializers.ModelSerializer):
    from_user = UserSerializer(read_only=True)
    to_user = UserSerializer(read_only=True)

    class Meta:
        model = Friendship
        fields = ["id", "from_user", "to_user", "is_accepted", "created_at"]
        read_only_fields = ["id", "from_user", "to_user", "created_at"]


class FriendshipSerializer(serializers.ModelSerializer):
    from_user = UserSerializer(read_only=True)
    to_user = UserSerializer(read_only=True)

    class Meta:
        model = Friendship
        fields = ["id", "from_user", "to_user", "is_accepted", "created_at"]
        read_only_fields = ["id", "created_at"]

    def create(self, validated_data):
        from_user = validated_data["from_user"]
        to_user = validated_data["to_user"]

        if from_user == to_user:
            raise serializers.ValidationError("You cannot friend yourself.")

        friendship = Friendship.objects.filter(
            from_user=from_user, to_user=to_user, is_accepted=False
        ).first()
        if friendship:
            raise serializers.ValidationError(
                "You already sent a friendship request to this user and it's still pending."
            )

        friendship_me_to_user = Friendship.objects.filter(
            from_user=from_user, to_user=to_user, is_accepted=True
        ).first()
        friendship_user_to_me = Friendship.objects.filter(
            from_user=to_user, to_user=from_user, is_accepted=True
        ).first()
        if friendship_me_to_user or friendship_user_to_me:
            raise serializers.ValidationError(
                "You already have a friendship with this user."
            )

        friendship = Friendship.objects.filter(
            from_user=to_user, to_user=from_user, is_accepted=False
        ).first()
        if friendship:
            raise serializers.ValidationError(
                "This user has sent you a pending friendship request. Use the update route instead."
            )

        return Friendship.objects.create(**validated_data)

    def update(self, instance, validated_data):
        is_accepted = validated_data.get("is_accepted", instance.is_accepted)

        if is_accepted and instance.is_accepted:
            raise serializers.ValidationError("Friendship is already accepted")
        instance.is_accepted = is_accepted
        instance.save()
        return instance
