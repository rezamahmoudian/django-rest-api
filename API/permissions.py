from rest_framework.permissions import BasePermission ,SAFE_METHODS


class IsSuperUser(BasePermission):

    def has_permission(self, request, view):
        return bool(request.user and request.user.is_superuser)


class IsStaffOrReadOnly(BasePermission):

    def has_permission(self, request, view):
        if request.user and request.user.is_staff:
            return True

        elif request.method in SAFE_METHODS:
            return True

        else:
            return False

