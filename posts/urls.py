from django.urls import path
from .views import PostView, PostDetailView, CommentView, LikeView

urlpatterns = [
    path("posts/", PostView.as_view()),
    path("posts/<int:pk>/", PostDetailView.as_view()),
    path("posts/<int:post_id>/comments/", CommentView.as_view()),
    path("posts/<uuid:post_id>/likes/", LikeView.as_view()),
]
