from rest_framework.permissions import BasePermission
from .models import Post


class IsPostOwnerOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method == "GET" and obj.access == "public":
            return True
        return obj.posted_by == request.user
