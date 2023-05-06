from django.urls import path
from .views import PostView, PostDetailView, CommentView, LikeView, UnlikeView, CommentDetailView

urlpatterns = [
    path("posts/", PostView.as_view()),
    path("posts/<uuid:pk>/", PostDetailView.as_view()),
    path("posts/<uuid:post_id>/comments/", CommentView.as_view()),
    path("posts/comments/<uuid:pk>", CommentDetailView.as_view()),
    path("posts/<uuid:post_id>/like/", LikeView.as_view()),
    path("posts/<uuid:post_id>/unlike/", UnlikeView.as_view()),
]
