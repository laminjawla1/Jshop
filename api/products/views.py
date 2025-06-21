from .serializers import ProductSerializer
from rest_framework import generics
from .models import Product
from users import authentication
from .permissions import ProductPermission
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status
from rest_framework.mixins import ListModelMixin, CreateModelMixin, UpdateModelMixin, DestroyModelMixin, RetrieveModelMixin


class ProductMixin(ListModelMixin, RetrieveModelMixin, CreateModelMixin, UpdateModelMixin, DestroyModelMixin, generics.GenericAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [ProductPermission, permissions.IsAuthenticatedOrReadOnly]

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
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        self.perform_create(serializer)

        return Response({
            "message": "Product successfully added.",
        }, status=status.HTTP_201_CREATED)
