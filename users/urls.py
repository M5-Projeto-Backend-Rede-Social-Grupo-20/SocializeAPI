from django.urls import path
from .views import UserView, UserDetailView
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path("user/", UserView.as_view()),
    path("user/<int:id>/", UserDetailView.as_view()),
    path("user/login/", jwt_views.TokenObtainPairView.as_view())
]