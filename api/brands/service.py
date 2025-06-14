from .models import Brand
from .serializers import BrandSerializer
from django.shortcuts import get_object_or_404


def get_brands():
    return BrandSerializer(Brand.objects.all()).data

def get_brand(brand_id) -> Brand:
    brand = get_object_or_404(Brand, id=brand_id)
    return BrandSerializer(brand).data

def add_brand(serialized_data):
    return BrandSerializer(serialized_data.save()).data
