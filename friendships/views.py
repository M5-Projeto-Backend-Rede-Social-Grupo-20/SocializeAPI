from django.forms import ValidationError
from rest_framework import generics, mixins, views
from rest_framework import permissions
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import serializers

from .serializers import FriendshipSerializer
from .models import Friendship
from users.models import User


class FriendshipSelfView(generics.ListAPIView):
    serializer_class = FriendshipSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        friendship_type = self.request.GET.get("type")
        if friendship_type == "pending":
            return Friendship.objects.filter(to=user, is_accepted=False)
        return Friendship.objects.filter(to_user=user, is_accepted=True)


class FriendshipView(generics.ListCreateAPIView, generics.DestroyAPIView):
    serializer_class = FriendshipSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        obj = get_object_or_404(User, id=self.kwargs["user_id"])
        return obj

    def get_queryset(self):
        user = self.get_object()

    def perform_create(self, serializer):
        user = self.get_object()
        return serializer.save(from_user=self.request.user, to_user=user)

    def perform_destroy(self, instance):
        user = self.get_object()
        friendship = Friendship.objects.filter(
            from_user=self.request.user, to_user=user, is_accepted=True
        )
        if not friendship:
            raise serializers.ValidationError("You are not friends with this user")
        friendship.delete()
