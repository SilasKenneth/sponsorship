from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return True

    def has_permission(self, request, view):
        return True


class ReadableAndWritableByEveryone(permissions.AllowAny):
    pass
