from django.forms import ValidationError
from rest_framework import generics, mixins, views
from rest_framework import permissions
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import serializers

from .serializers import FollowSerializer
from .models import Follow
from users.models import User


class FollowSelfView(generics.ListAPIView):
    serializer_class = FollowSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        follows_type = self.request.GET.get("type")
        if follows_type == "following":
            return Follow.objects.filter(from_user=user)
        return Follow.objects.filter(to_user=user)


class FollowView(generics.ListCreateAPIView, generics.DestroyAPIView):
    serializer_class = FollowSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        obj = get_object_or_404(User, id=self.kwargs["user_id"])
        return obj

    def get_queryset(self):
        user = self.get_object()
        follows_type = self.request.GET.get("type")
        if follows_type == "following":
            return Follow.objects.filter(from_user=user)
        elif follows_type == "check":
            return Follow.objects.filter(from_user=self.request.user, to_user=user)
        return Follow.objects.filter(to_user=user)

    def perform_create(self, serializer):
        user = self.get_object()
        return serializer.save(from_user=self.request.user, to_user=user)

    def perform_destroy(self, instance):
        user = self.get_object()
        follow = Follow.objects.filter(from_user=self.request.user, to_user=user)
        if not follow:
            raise serializers.ValidationError("You not follow this user.")
        follow.delete()
