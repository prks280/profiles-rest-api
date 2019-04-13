from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    """allow users to update their profile"""

    def has_object_permission(self, request,view,obj):

        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.id == request.user.id

