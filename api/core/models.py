from django.db import models
from django_tenants.models import TenantMixin, DomainMixin
from utils.base import BaseModel


class Client(TenantMixin, BaseModel):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    auto_create_schema = True
    auto_drop_schema = True

    def __str__(self):
        return self.name 


class Domain(DomainMixin, BaseModel):
    pass


class TenantUserRegistry(BaseModel):
    class Meta:
        ordering = ("tenant",)
        verbose_name_plural = "Tenant User Registries"
    email = models.EmailField(unique=True)
    tenant = models.ForeignKey(Client, on_delete=models.CASCADE)