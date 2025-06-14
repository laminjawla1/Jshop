from django.contrib import admin
from . models import Category


@admin.register(Category)
class BrandAdmin(admin.ModelAdmin):
    list_display = ["name"]