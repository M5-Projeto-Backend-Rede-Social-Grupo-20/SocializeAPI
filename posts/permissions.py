from rest_framework.permissions import BasePermission
from .models import Post


class IsPostOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        if obj.access == "public":
            return True
        return obj.posted_by == request.user


class IsCommentOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method == "GET" and obj.post.access == "public":
            return True
        if request.method == "DELETE":
            return obj.commented_by == request.user
