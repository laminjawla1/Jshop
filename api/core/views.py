from django.conf import settings
from django.db import IntegrityError
from django.contrib.auth import authenticate
from django_tenants.utils import schema_context

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.generics import CreateAPIView
from rest_framework.exceptions import ValidationError

from users.models import User
from settings.models import Setting
from locations.models import Location
from currencies.models import Currency

from core.models import Client, Domain
from core.models import TenantUserRegistry
from core.serializers import TenantSignupSerializer


class ClientCreateAPIView(CreateAPIView):
    serializer_class = TenantSignupSerializer

    def perform_create(self, serializer):
        data = serializer.validated_data

        # Check if this domain name already exists
        if Client.objects.filter(schema_name=data['subdomain']).exists():
            raise ValidationError({"error": "A business with this domain name already exists."})

        # Create the tenant
        tenant = Client(
            schema_name=data["subdomain"],
            name=data["business_name"],
            email=data["email"]
        )
        tenant.save()

        # Create its domain (e.g., jawlacosmetics.localhost)
        Domain.objects.create(
            domain=f"{data['subdomain']}.{settings.BASE_URL}",
            tenant=tenant,
            is_primary=True
        )

        # Create some default settings for the tenant
        with schema_context(tenant.schema_name):
            try:
                User.objects.create_superuser(
                    first_name=data["first_name"],
                    last_name=data["last_name"],
                    email=data["email"],
                    username=data["email"],
                    phone_number=data["phone_number"],
                    password=data["password"],
                )
            except IntegrityError:
                raise ValidationError({"error": "A user with this email already exists."})
            
            # Create a default location
            Location.objects.create(name="Head Office")

            # Settings
            default_currency = Currency.objects.first()
            Setting.objects.create(default_currency=default_currency)

        # Register a tenant
        TenantUserRegistry.objects.create(email=data["email"], tenant=tenant)

        return tenant
        
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        self.perform_create(serializer)

        return Response({
            "message": "Business profile and admin user created successfully.",
            "login_url": f"http://{settings.BASE_URL}{settings.PORT}/api/users/login"
        }, status=status.HTTP_201_CREATED)
    


class GlobalLoginAPIView(APIView):
    def post(self, request):
        email = request.data.get("email")
        password = request.data.get("password")

        if not email or not password:
            return Response({"error": "Email and password are required."}, status=status.HTTP_400_BAD_REQUEST)

        # STEP 1: Lookup tenant from global registry (public schema)
        try:
            registry = TenantUserRegistry.objects.get(email=email)
            tenant_schema = registry.tenant.schema_name
        except TenantUserRegistry.DoesNotExist:
            return Response({"error": "No tenant found for this email."}, status=status.HTTP_404_NOT_FOUND)

        # STEP 2: Switch to tenant schema and authenticate
        with schema_context(tenant_schema):
            user = authenticate(username=email, password=password)
            if not user:
                return Response({"error": "Invalid credentials."}, status=status.HTTP_401_UNAUTHORIZED)

            token, _ = Token.objects.get_or_create(user=user)

            return Response({
                "token": token.key,
                "tenant": tenant_schema,
                "BASE_URL": f"http://{tenant_schema}.{settings.BASE_URL}{settings.PORT}/api/"
            })

        