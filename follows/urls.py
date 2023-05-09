from django.urls import path
from .views import (
    FollowerSelfView,
    FollowingSelfView,
    FollowView,
    FollowerView,
    FollowingView,
)

urlpatterns = [
    path("follows/followers", FollowerSelfView.as_view()),
    path("follows/following", FollowingSelfView.as_view()),
    path("follows/<uuid:user_id>/", FollowView.as_view()),
    path("follows/<uuid:user_id>/followers", FollowerView.as_view()),
    path("follows/<uuid:user_id>/following", FollowingView.as_view()),
]
