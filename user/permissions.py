from rest_framework import permissions


class ReadOnly(permissions.BasePermission):
    """
    Allow us to read only endpoints
    """
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
