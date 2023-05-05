from django.urls import path
from .views import PostView, PostDetailView

urlpatterns = [
    path("posts/", PostView.as_view()),
    path("posts/<int:pk>/", PostDetailView.as_view()),
]
