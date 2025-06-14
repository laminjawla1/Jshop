from .models import Brand
from rest_framework import serializers


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ["id", "name", "owner", "created_at", "updated_at"]
        read_only_fields = ("owner",)