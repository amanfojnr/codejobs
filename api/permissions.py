from rest_framework.permissions import BasePermission
from rest_framework import permissions
from .models import Listing


class IsCompanyOrReadOnly(BasePermission):
    """
    Custom permission to allow only listing company to edit job listing
    """

    def has_object_permission(self, request, view, obj):
        """
        Return True, if permission is granted by the owner
        """
        if request.method in permissions.SAFE_METHODS:
            return True

        if isinstance(obj, Listing):
            return obj.company == request.user.company
        return obj.company == request.user.company
