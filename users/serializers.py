from rest_framework import serializers
from django.core.exceptions import ValidationError

from .models import User


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "email",
            "password",
            "first_name",
            "last_name",
            "birthdate",
            "bio",
            "gender",
            "city",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["id", "created_at", "updated_at"]
        extra_kwargs = {
            "email": {"required": True},
            "username": {"required": True},
            "password": {"required": True, "write_only": True},
            "first_name": {"required": True},
            "last_name": {"required": True},
            "bio": {"allow_null": True},
            "birthdate": {"allow_null": True},
            "city": {"allow_null": True},
            "gender": {"required": False},
        }

    def validate_username(self, username):
        if User.objects.filter(username=username).exists():
            raise ValidationError("A user with that username already exists.")
        return username

    def validate_email(self, email):
        if User.objects.filter(email=email).exists():
            raise ValidationError("A user with that email already exists.")
        return email

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

    def update(self, instance, validated_data):
        password = validated_data.pop("password", None)

        for key, value in validated_data.items():
            setattr(instance, key, value)

        if password is not None:
            instance.set_password(password)

        instance.save()
        return instance
