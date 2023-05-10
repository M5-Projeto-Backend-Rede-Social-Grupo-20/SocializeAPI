from django.urls import path
from .views import PostView, PostDetailView, UserPostView

urlpatterns = [
    path("posts/", PostView.as_view()),
    path("posts/<uuid:pk>/", PostDetailView.as_view()),
    path("users/posts/<uuid:user_id>/", UserPostView.as_view()),
]
