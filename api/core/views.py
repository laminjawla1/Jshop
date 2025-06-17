from rest_framework.generics import CreateAPIView
from .models import Client, Domain
from .serializers import TenantSignupSerializer
from rest_framework.exceptions import ValidationError
from django.db import IntegrityError
from users.models import User
from rest_framework.response import Response
from rest_framework import status
from django.core.management import call_command
from django.conf import settings
from django_tenants.utils import schema_context

from rest_framework.views import APIView
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from .models import TenantUserRegistry

class ClientCreateAPIView(CreateAPIView):
    serializer_class = TenantSignupSerializer

    def perform_create(self, serializer):
        try:
            data = serializer.validated_data

            # 1. Sterilize the schema from the domain name
            schema_name = data['domain_name'].lower().replace(" ", "")
            domain_prefix = schema_name

            # 2. Check if this domain name already exists
            if Client.objects.filter(schema_name=schema_name).exists():
                raise ValidationError({"error": "A business with this domain name already exists."})

            # 3. Check if this user already exists
            if User.objects.filter(email=data["email"]).exists():
                raise ValidationError({"error": "A user with this email already exists."})

            # 4. Create the tenant
            tenant = Client(
                schema_name=data["domain_name"],
                name=data["business_name"],
                email=data["email"]
            )
            tenant.save()
            call_command("migrate_schemas", schema_name=tenant.schema_name)

            # 5. Create its domain (e.g., jawlacosmetics.localhost)
            Domain.objects.create(
                domain=f"{domain_prefix}.{settings.BASE_URL}",
                tenant=tenant,
                is_primary=True
            )

            # 6. Create a user
            with schema_context(tenant.schema_name):
                User.objects.create_user(
                    first_name=data["first_name"],
                    last_name=data["last_name"],
                    email=data["email"],
                    username=data["email"],
                    phone_number=data["phone_number"],
                    password=data["password"],
                )
            
            TenantUserRegistry.objects.create(email=data["email"], tenant=tenant)

            return tenant
        except IntegrityError as e:
            raise ValidationError({"error": "A business with this domain name already exists."})
        
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        tenant = self.perform_create(serializer)
        return Response({
            "message": "Tenant and user created successfully.",
            "tenant": tenant.name,
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

        