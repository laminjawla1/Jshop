from rest_framework import permissions


class VendorPermission(permissions.DjangoModelPermissions):
    # perms_map = {
    #     'GET': [],
    #     'OPTIONS': [],
    #     'HEAD': [],
    #     'POST': ['%(app_label)s.add_%(model_name)s'],
    #     'PUT': ['%(app_label)s.change_%(model_name)s'],
    #     'PATCH': ['%(app_label)s.change_%(model_name)s'],
    #     'DELETE': ['%(app_label)s.delete_%(model_name)s'],
    # }
    def has_permission(self, request, view):
        user = request.user
        if user.is_vendor or user.is_staff:
            return True
        return False