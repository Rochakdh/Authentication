from rest_framework.permissions import BasePermission, SAFE_METHODS


class CustomIsAuthenticated(BasePermission):
    message = 'Access Denied'

    def has_object_permission(self, request, view, obj):
        """
        Object level permission to the UserViewSet allowing all users to use SAFE_METHODS
        and only allow owner to modify it
        :return: boolean true or false
        """
        print(dir(view))
        if request.method in SAFE_METHODS:
            # Check permissions for read-only request i.e. allow get,option,head for non authenticated user as well
            return True
        return request.user == obj  # else put,patch are allowed to the owner of the instance of class only
