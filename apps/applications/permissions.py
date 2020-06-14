from rest_framework import permissions
from rest_framework_simplejwt.models import TokenUser


class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.is_anonymous:
            return False
        if not request.auth.get('is_student'):
            return False
        if request.auth.get('id') != obj.user_id:
            return False
        return True

    def has_permission(self, request, view):
        if request.user.is_anonymous:
            return False
        return True


class StaffCanDoAnythingToApplications(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return self.has_permission(request, view)

    def has_permission(self, request, view):
        if request.user.is_anonymous:
            return False
        if request.auth.get('is_staff'):
            return True
        return False


class StudentSubmitApplicationPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return self.has_permission(request, view)

    def has_permission(self, request, view):
        if request.user.is_anonymous or not request.user.is_authenticated:
            return False
        if request.auth.get('is_student'):
            return True
        return False

