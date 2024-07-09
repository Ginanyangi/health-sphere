from rest_framework.permissions import BasePermission

class IsAdminUser(BasePermission):
    def has_permission(self, request, view):
        if not request.user or not request.user.is_authenticated:
            return False
        # Check if the user has the required role
        return request.user.role in ['admin', 'superadmin']
        # return request.user and request.user.role in ['admin', 'superadmin']

class IsStaffUser(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.role == 'staff'