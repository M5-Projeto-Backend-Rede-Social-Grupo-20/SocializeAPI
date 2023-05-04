from rest_framework.permissions import BasePermission
from .models import Post


class IsPostOwnerOrReadOnly:
    def has_permission(self, request, view, obj: Post):
        if request.method == "GET":
            return True
        return obj.posted_by == request.user
