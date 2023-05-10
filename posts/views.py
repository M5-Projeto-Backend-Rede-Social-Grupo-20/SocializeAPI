from django.shortcuts import get_object_or_404
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
    ListAPIView,
)
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated

from .models import Post
from .serializers import PostSerializer
from .permissions import IsPostOwner
from users.models import User
from friendships.models import Friendship


class PostView(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        return serializer.save(posted_by=self.request.user)

    def get_queryset(self):
        return Post.objects.filter(access="public")


class UserPostView(ListAPIView):
    serializer_class = PostSerializer
    authentication_classes = [JWTAuthentication]

    def get_object(self):
        obj = get_object_or_404(User, id=self.kwargs["user_id"])
        return obj

    def get_queryset(self):
        from_user = self.request.user
        to_user = self.get_object()

        if not from_user.is_authenticated:
            return to_user.posts.all().filter(access="public")

        if from_user == to_user:
            return to_user.posts.all()

        friendship_me_to_user = Friendship.objects.filter(
            from_user=from_user, to_user=to_user, is_accepted=True
        ).first()
        friendship_user_to_me = Friendship.objects.filter(
            from_user=to_user, to_user=from_user, is_accepted=True
        ).first()
        follow_user = (
            to_user.followers.all().filter(from_user=self.request.user).first()
        )

        if friendship_me_to_user or friendship_user_to_me or follow_user:
            return to_user.posts.all()
        return to_user.posts.all().filter(access="public")


class PostDetailView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly, IsPostOwner]

    queryset = Post.objects.all()
    serializer_class = PostSerializer
