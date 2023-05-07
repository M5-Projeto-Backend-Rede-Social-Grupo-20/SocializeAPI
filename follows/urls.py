from django.urls import path
from .views import FollowSelfView, FollowView

urlpatterns = [
    path("follows/", FollowSelfView.as_view()),
    path("follows/<uuid:user_id>/", FollowView.as_view()),
]
