from rest_framework import generics
from rest_framework import permissions
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
            return user.following.all()
        return user.followers.all()


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
            return user.followings.all()
        elif follows_type == "check":
            return user.followers.all().filter(from_user=self.request.user)
        return user.followers.all()

    def perform_create(self, serializer):
        user = self.get_object()
        return serializer.save(from_user=self.request.user, to_user=user)

    def perform_destroy(self, instance):
        user = self.get_object()
        follow = user.followers.filter(from_user=self.request.user).first()
        if not follow:
            raise serializers.ValidationError("You not follow this user.")
        follow.delete()
