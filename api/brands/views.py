from rest_framework import generics
from . import permissions
from rest_framework import authentication
from rest_framework.mixins import ListModelMixin, CreateModelMixin, UpdateModelMixin, DestroyModelMixin, RetrieveModelMixin

from .models import Brand
from brands.serializers import BrandSerializer


class BrandMixin(ListModelMixin, RetrieveModelMixin, CreateModelMixin, UpdateModelMixin, DestroyModelMixin, generics.GenericAPIView):
    # queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.IsStaffEditorPermission]

    def get_queryset(self):
        print(self.request.user)
        brands = Brand.objects.all()[:2]
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
