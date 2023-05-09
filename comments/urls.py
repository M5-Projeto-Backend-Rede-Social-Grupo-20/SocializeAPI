from django.urls import path
from .views import CommentView, CommentDetailView

urlpatterns = [
    path("posts/<uuid:post_id>/comments/", CommentView.as_view()),
    path("posts/comments/<uuid:pk>", CommentDetailView.as_view()),
]
