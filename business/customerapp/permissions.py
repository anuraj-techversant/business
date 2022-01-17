"""
The permisions.py define the cutomised permissions
"""
from rest_framework import permissions

class IsAuthenticatedUser(permissions.BasePermission):
    """
    The permission is override here. IsAuthenticatedUser is defined in permisssion class
    following function is executed.
    """

    def has_permission(self, request, view):
        """ 
        The GET request is override so that all users can access(authorised 
        and unauthorised). authorised users are allowed to perform other 
        requests(POST, PUT, DELETE). 
        """
        if request.method == 'GET':
            return True
        return request.user and request.user.is_authenticated
