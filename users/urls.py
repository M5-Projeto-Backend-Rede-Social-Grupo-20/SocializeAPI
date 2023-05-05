from django.urls import path
from .views import UserListView, UserDetailView
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path("user/", UserListView.as_view()),
    path("user/<uuid:id>/", UserDetailView.as_view()),
    path("user/login/", jwt_views.TokenObtainPairView.as_view()),
    path("user/refresh/", jwt_views.TokenRefreshView.as_view()),
]
