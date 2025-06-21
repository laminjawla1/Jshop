from .serializers import CategorySerializer
from rest_framework import generics
from .models import Category
from users import authentication
from .permissions import CategoryPermission
from rest_framework import permissions
from rest_framework.mixins import ListModelMixin, CreateModelMixin, UpdateModelMixin, DestroyModelMixin, RetrieveModelMixin


class CategoryMixin(ListModelMixin, RetrieveModelMixin, CreateModelMixin, UpdateModelMixin, DestroyModelMixin, generics.GenericAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [CategoryPermission, permissions.IsAuthenticatedOrReadOnly]

    def get(self, request, *args, **kwargs):
        if kwargs.get("pk"):
            return self.retrieve(request, args, kwargs)
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
