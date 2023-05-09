from rest_framework.permissions import BasePermission


class IsCommentOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method == "GET" and obj.post.access == "public":
            return True
        if request.method == "DELETE":
            return obj.commented_by == request.user
