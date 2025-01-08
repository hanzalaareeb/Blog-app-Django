from rest_framework import permissions

class IsAuthorOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        # Authenticated users can only vioew list
        if request.user.is_authenticated:
            return True
        return False
    def has_object_permission(self, request, view, obj):
        # read permission is allowed so we will always
        # allow GET, HEAD , or OPTIONS request
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user