from rest_framework import permissions
from rest_framework.views import Request, View


class IsAdminOrGet(permissions.BasePermission):
    def has_permission(self, request, view):

        return (
            request.method in permissions.SAFE_METHODS
            or request.user.is_superuser
        )


class IsAdminOrOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.is_superuser:
            return True
        else:
            if request.method in permissions.SAFE_METHODS:
                pass
            return request.method in permissions.SAFE_METHODS
