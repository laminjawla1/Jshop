from .serializers import UnitSerializer
from rest_framework import generics
from .models import Unit
from rest_framework import permissions
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin


class UnitMixin(ListModelMixin, RetrieveModelMixin, generics.GenericAPIView):
    queryset = Unit.objects.all()
    serializer_class = UnitSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request, *args, **kwargs):
        if kwargs.get("pk"):
            return self.retrieve(request, args, kwargs)
        return self.list(request, *args, **kwargs)
