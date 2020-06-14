from django.contrib.auth.models import AnonymousUser
from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user == AnonymousUser:
            return False
        if request.user.is_student:
            return False
        if request.user.id != obj.user_id:
            return False
        return True

    def has_permission(self, request, view):
        if request.user == AnonymousUser:
            return False
        return True


class StaffCanDoAnythingToApplications(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return self.has_permission(request, view)

    def has_permission(self, request, view):
        if request.user == AnonymousUser:
            return False
        if request.user.is_staff:
            return True
        return False
