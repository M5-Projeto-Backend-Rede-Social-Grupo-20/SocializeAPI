from rest_framework import generics, permissions
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import serializers

from .serializers import (
    FollowersListSerializer,
    FollowingListSerializer,
    FollowCreateSerializer,
)
from users.models import User


class FollowerSelfView(generics.ListAPIView):
    serializer_class = FollowersListSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return user.followers.all()


class FollowingSelfView(generics.ListAPIView):
    serializer_class = FollowingListSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return user.following.all()


class FollowView(generics.CreateAPIView, generics.DestroyAPIView):
    serializer_class = FollowCreateSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        obj = get_object_or_404(User, id=self.kwargs["user_id"])
        return obj

    def perform_create(self, serializer):
        user = self.get_object()
        return serializer.save(from_user=self.request.user, to_user=user)

    def perform_destroy(self, instance):
        user = self.get_object()
        follow = user.followers.filter(from_user=self.request.user).first()
        if not follow:
            raise serializers.ValidationError("You not follow this user.")
        follow.delete()


class FollowerView(generics.ListAPIView):
    serializer_class = FollowersListSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        obj = get_object_or_404(User, id=self.kwargs["user_id"])
        return obj

    def get_queryset(self):
        user = self.get_object()
        return user.followers.all()


class FollowingView(generics.ListAPIView):
    serializer_class = FollowingListSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        obj = get_object_or_404(User, id=self.kwargs["user_id"])
        return obj

    def get_queryset(self):
        user = self.get_object()
        return user.following.all()
