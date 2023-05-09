from django.urls import path
from .views import (
    FriendshipSelfView,
    FriendshipSelfReceivedPendingView,
    FriendshipView,
    FriendshipUpdateView,
    FriendshipDestroyView,
)

urlpatterns = [
    path(
        "friendships/",
        FriendshipSelfView.as_view(),
        name="friendship-request-list",
    ),
    path(
        "friendships/received-pending",
        FriendshipSelfReceivedPendingView.as_view(),
        name="friendship-request-list",
    ),
    path(
        "friendships/<uuid:user_id>/",
        FriendshipView.as_view(),
        name="friendship-detail",
    ),
    path(
        "friendships/<uuid:user_id>/accept/",
        FriendshipUpdateView.as_view(),
        name="friendship-request-accept",
    ),
    path(
        "friendships/<uuid:user_id>/reject/",
        FriendshipDestroyView.as_view(),
        name="friendship-request-reject",
    ),
]
