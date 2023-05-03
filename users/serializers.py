from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    def update(self, instance: User, validated_data: dict) -> User:
        for key, value in validated_data.items():
            setattr(instance, key, value)
            if key == "password":
                instance.set_password(validated_data["password"])
        instance.save()
        return instance

    def create(self, validated_data: dict) -> User:
        return User.objects.create_user(**validated_data)
    
    class Meta:
        model = User
        fields = "__all__"
        extra_kwargs = {"password": {"write_only": True}}
