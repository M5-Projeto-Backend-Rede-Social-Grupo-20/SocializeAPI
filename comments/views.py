from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from .models import Comment
from .serializers import CommentSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from posts.models import Post
from django.shortcuts import get_object_or_404


class CommentView(CreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def perform_create(self, serializer):
        post = get_object_or_404(Post, id=self.kwargs["post_id"])
        return serializer.save(post=post, commented_by=self.request.user)
