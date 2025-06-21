from django.contrib import admin
from .models import Unit


@admin.register(Unit)
class UnitAdmin(admin.ModelAdmin):
    list_display = ["name", "symbol", "created_at", "updated_at"]
    ordering = ("name",)