from .serializers import CurrencySerializer
from rest_framework import generics
from .models import Currency
from rest_framework import permissions
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin


class CurrencyMixin(ListModelMixin, RetrieveModelMixin, generics.GenericAPIView):
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request, *args, **kwargs):
        if kwargs.get("pk"):
            return self.retrieve(request, args, kwargs)
        return self.list(request, *args, **kwargs)
