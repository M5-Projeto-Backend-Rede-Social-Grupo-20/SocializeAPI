from django.urls import path
from .views import LikeView, UnlikeView


urlpatterns = [
    path("posts/<uuid:post_id>/likes/", LikeView.as_view()),
    path("posts/<uuid:post_id>/unlike/", UnlikeView.as_view()),
]
