from django.urls import path
from .views import PostView, PostDetailView

urlpatterns = [
    path("posts/", PostView.as_view()),
    path("posts/<int:post_id>/", PostDetailView.as_view()),
]
