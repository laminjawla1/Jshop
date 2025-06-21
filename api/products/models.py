from django.db import models
from utils.base import BaseModel
from categories.models import Category
from brands.models import Brand
from locations.models import Location
from units.models import Unit


class Product(BaseModel):
    """Representation of a product entity"""
    class Meta:
        ordering = ("name",)

    image = models.ImageField(upload_to="product_images", null=False, blank=False)
    name = models.CharField(max_length=120, null=False, blank=False)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    units = models.ManyToManyField(Unit, blank=True)
    categories = models.ManyToManyField(Category, related_name="products")
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name="products")
    description = models.TextField(blank=True, null=True)
    location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True)

    def __str__(self) -> str:
        return str(self.name)
