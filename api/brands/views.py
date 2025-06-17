from rest_framework import generics
from . import permissions
from rest_framework.mixins import ListModelMixin, CreateModelMixin, UpdateModelMixin, DestroyModelMixin, RetrieveModelMixin
from users import authentication
from .models import Brand
from rest_framework import permissions
from brands.serializers import BrandSerializer


class BrandListCreateAPIView(generics.ListCreateAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class BrandMixin(ListModelMixin, RetrieveModelMixin, CreateModelMixin, UpdateModelMixin, DestroyModelMixin, generics.GenericAPIView):
    # queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    # permission_classes = [permissions.IsStaffEditorPermission]

    def get_queryset(self):
        brands = Brand.objects.all()
        return brands

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
    
    def perform_create(self, serializer):
        serializer.validated_data["owner"] = self.request.user
        if serializer.is_valid(raise_exception=True):
            return serializer.save()
