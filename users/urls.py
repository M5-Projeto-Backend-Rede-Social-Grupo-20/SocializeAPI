from django.urls import path
from .views import UserListView, UserDetailView
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path("users/", UserListView.as_view()),
    path("users/<uuid:user_id>/", UserDetailView.as_view()),
    path("users/login/", jwt_views.TokenObtainPairView.as_view()),
    path("users/refresh/", jwt_views.TokenRefreshView.as_view()),
]
