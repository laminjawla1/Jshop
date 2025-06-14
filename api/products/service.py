from . models import Product
from django.shortcuts import get_object_or_404


def get_products():
    """
        Query the entire products model and sort them in descending order by created_at
        and then return a list of serialized products
    """
    return [product.serialize() for product in Product.objects.all()]

def get_product(product_id) -> Product:
    return get_object_or_404(Product, id=product_id)

def add_product(product):
    return Product.objects.create(**product)