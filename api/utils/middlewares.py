# middleware/block_public_schema.py

from django.http import HttpResponseNotFound
from django_tenants.utils import get_tenant

class BlockPublicSchemaMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        tenant = get_tenant(request)
        if tenant.schema_name == 'public':
            return HttpResponseNotFound("This page isn't available.")
        return self.get_response(request)
