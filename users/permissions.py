from rest_framework import permissions
from rest_framework.views import Request, View
from .models import User


class IsUserOnwerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request: Request, view: View, obj: User) -> bool:
        return (
            request.method in permissions.SAFE_METHODS
            or request.user
            and request.user.is_authenticated
            and request.user == obj
        )
