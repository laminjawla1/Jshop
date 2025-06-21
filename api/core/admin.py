from django.contrib import admin
from . models import Domain, Client as Tenant, TenantUserRegistry


@admin.register(Tenant)
class TenantAdmin(admin.ModelAdmin):
    list_display = ["name", "email", "schema_name", "created_at", "updated_at"]

@admin.register(Domain)
class DomainAdmin(admin.ModelAdmin):
    list_display = ["domain", "tenant", "is_primary", "created_at", "updated_at"]

@admin.register(TenantUserRegistry)
class TenantUserRegistryAdmin(admin.ModelAdmin):
    list_display = ["email", "tenant", "created_at", "updated_at"]