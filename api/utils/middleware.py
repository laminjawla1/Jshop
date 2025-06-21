from django_tenants.middleware.main import TenantMainMiddleware
from django.http import JsonResponse
from core.models import Domain


class CustomTenantMiddleware(TenantMainMiddleware):
    def process_request(self, request):
        try:
            super().process_request(request)
        except Domain.DoesNotExist:
            return JsonResponse({
                "error": "Invalid subdomain. Tenant not found."
            }, status=404)
