
from  rest_framework.permissions import  BasePermission,SAFE_METHODS
from rest_framework.permissions import DjangoModelPermissions


class IsOwnerOrReadOnly(BasePermission):
    message='not allowed'
    my_safe_mehod=['GET','POST','PATCH','DELETE']
    def has_permission(self, request, view):
        if request.method in self.my_safe_mehod:
            return True
        else:
            return False

    def has_object_permission(self, request, view,obj):


        if request.method in SAFE_METHODS:
            return True

        return obj.user == request.user


class WithViewDjangoModelPermissions(DjangoModelPermissions):
    perms_map = {
        'GET': ['%(app_label)s.view_%(model_name)s'],
        'OPTIONS': [],
        'HEAD': [],
        'POST': ['%(app_label)s.add_%(model_name)s'],
        'PUT': ['%(app_label)s.change_%(model_name)s'],
        'PATCH': ['%(app_label)s.change_%(model_name)s'],
        'DELETE': ['%(app_label)s.delete_%(model_name)s'],
    }




