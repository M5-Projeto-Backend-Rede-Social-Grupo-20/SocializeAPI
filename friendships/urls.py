from django.urls import path
from .views import FriendshipView

urlpatterns = [
    path("friendships/", FriendshipView.as_view()),
]
