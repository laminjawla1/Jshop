from django.db import models
from utils.base import BaseModel
from users.models import User
from categories.models import Category
from brands.models import Brand
from locations.models import Location


class ProductUnit(BaseModel):
    unit = models.CharField(max_length=16)

    def __str__(self) -> str:
        return str(self.unit)


class Product(BaseModel):
    """Representation of a product entity"""
    class Meta:
        ordering = ("-created_at",)

    image = models.ImageField(upload_to="product_images")
    name = models.CharField(max_length=120, null=False, blank=False)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    unit = models.ForeignKey(ProductUnit, on_delete=models.DateTimeField, null=True)
    categories = models.ManyToManyField(Category, related_name="products")
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name="products")
    description = models.TextField(blank=True, null=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="products")
    location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True)

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "price": self.price,
            "description": self.description,
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }

    def __str__(self) -> str:
        return str(self.name)


# class ProductImage(BaseModel):
#     product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="images")
#     image = models.ImageField(upload_to="product_images")

#     def __str__(self) -> str:
#         return str(self.product)