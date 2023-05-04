from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveDestroyAPIView
from .serializers import PostSerializer
from .models import Post
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from .permissions import IsPostOwnerOrReadOnly


class PostView(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        return serializer.save(posted_by=self.request.user)


class PostDetailView(RetrieveDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = []

    queryset = Post.objects.all()
    serializer_class = PostSerializer
