from django.shortcuts import render
from rest_framework.generics import (
    ListCreateAPIView,
    DestroyAPIView,
)
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import (
    IsAuthenticatedOrReadOnly,
    IsAuthenticated,
    IsAuthenticatedOrReadOnly,
)
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import NotFound

from .models import Like
from .serializers import LikeSerializer
from posts.models import Post


class LikeView(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    queryset = Like.objects.all()
    serializer_class = LikeSerializer

    def perform_create(self, serializer):
        post = get_object_or_404(Post, id=self.kwargs["post_id"])
        like = Like.objects.filter(liked_by_id=self.request.user.id, post=post)

        if like.exists():
            return Response(
                {"detail": "This post was already liked"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        serializer.save(liked_by=self.request.user, post=post)


class UnlikeView(DestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Like.objects.all()
    serializer_class = LikeSerializer

    def get_object(self):
        try:
            like = Like.objects.get(
                post_id=self.kwargs["post_id"], liked_by=self.request.user
            )
        except Like.DoesNotExist:
            raise NotFound("This post was not liked")

        return like
