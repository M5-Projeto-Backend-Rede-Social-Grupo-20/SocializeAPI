from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import PostSerializer
from .models import Post
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .permissions import IsPostOwnerOrReadOnly


class PostView(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        return serializer.save(posted_by=self.request.user)

    def get_queryset(self):
        return Post.objects.filter(access="public")


class PostDetailView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsPostOwnerOrReadOnly]

    queryset = Post.objects.all()
    serializer_class = PostSerializer
