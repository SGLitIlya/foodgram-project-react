from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.IsAuthenticatedOrReadOnly):
    """Anonymous user can read.
    Authenticated user can create.
    Owner can change.
    """

    def has_object_permission(self, request, view, obj):
        return (
            request.method in permissions.SAFE_METHODS
            or obj.author == request.user
        )
