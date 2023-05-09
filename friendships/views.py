from django.forms import ValidationError
from rest_framework import generics, mixins, views, serializers
from rest_framework import permissions
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.db.models import Q

from .serializers import FriendshipSerializer
from .models import Friendship
from users.models import User


class FriendshipSelfView(generics.ListAPIView):
    serializer_class = FriendshipSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Friendship.objects.filter(
            Q(from_user=user) | Q(to_user=user), is_accepted=True
        )


class FriendshipSelfReceivedPendingView(generics.ListAPIView):
    serializer_class = FriendshipSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Friendship.objects.filter(to=user, is_accepted=False)


class FriendshipView(generics.CreateAPIView):
    serializer_class = FriendshipSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        obj = get_object_or_404(User, id=self.kwargs["user_id"])
        return obj

    def perform_create(self, serializer):
        user = self.get_object()
        return serializer.save(from_user=self.request.user, to_user=user)


class FriendshipUpdateView(generics.UpdateAPIView):
    serializer_class = FriendshipSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    queryset = Friendship.objects.all()

    def get_object(self):
        obj = get_object_or_404(User, id=self.kwargs["user_id"])
        return obj

    def perform_update(self, serializer):
        from_user = self.request.user
        to_user = self.get_object()
        friendship = Friendship.objects.filter(
            from_user=to_user, to_user=from_user, is_accepted=False
        ).first()
        if not friendship:
            raise serializers.ValidationError("Friendship not found.")
        friendship.is_accepted = True
        friendship.save()


class FriendshipDestroyAPIView(generics.UpdateAPIView):
    serializer_class = FriendshipSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    queryset = Friendship.objects.all()

    def get_object(self):
        obj = get_object_or_404(User, id=self.kwargs["user_id"])
        return obj

    def perform_destroy(self, instance):
        from_user = self.request.user
        to_user = self.get_object()
        friendship_me_to_user = Friendship.objects.filter(
            from_user=from_user, to_user=to_user, is_accepted=True
        ).first()
        friendship_user_to_me = Friendship.objects.filter(
            from_user=to_user, to_user=from_user, is_accepted=True
        ).first()
        if not friendship_me_to_user and not friendship_user_to_me:
            raise serializers.ValidationError("Friendship not found.")
        if friendship_me_to_user:
            friendship_me_to_user.delete()
        friendship_user_to_me.delete()
