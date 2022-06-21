from rest_framework.permissions import BasePermission, SAFE_METHODS


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


class IsAuthorOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.is_authenticated and \
                request.user.is_superuser:
            return True
        elif request.user.is_authenticated and \
                request.user == obj.author:
            return True
        elif request.method in SAFE_METHODS:
            return True
        else:
            return False


class IsSuperuserOrStaffReadOnly(BasePermission):

    def has_permission(self, request, view):
        if request.method in SAFE_METHODS and \
                request.user and request.user.is_staff:
            return True
        elif request.user.is_superuser:
            return True
        else:
            return False
