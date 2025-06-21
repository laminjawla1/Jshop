from .serializers import UserSerializer
from rest_framework import generics
from .models import User
from . import authentication
from .permissions import UserPermission
from rest_framework import permissions
from rest_framework.mixins import ListModelMixin, CreateModelMixin, UpdateModelMixin, DestroyModelMixin, RetrieveModelMixin


class UserMixin(ListModelMixin, RetrieveModelMixin, CreateModelMixin, UpdateModelMixin, DestroyModelMixin, generics.GenericAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [UserPermission, permissions.IsAuthenticatedOrReadOnly]

    def get(self, request, *args, **kwargs):
        if kwargs.get("pk"):
            return self.retrieve(request, args, kwargs)
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
