from rest_framework.permissions import BasePermission


class IsPostOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        if obj.access == "public":
            return True
        return obj.posted_by == request.user
