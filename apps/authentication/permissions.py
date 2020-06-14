from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return True

    def has_permission(self, request, view):
        print(request.user)
        return True


class StaffStudentViewOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        pass

    def has_permission(self, request, view):
        pass


class ReadableAndWritableByEveryone(permissions.AllowAny):
    pass
