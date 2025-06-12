from django.db import models
from utils.base import BaseModel


class Product(BaseModel):
    """Representation of a product entity"""

    name = models.CharField(max_length=120, null=False, blank=False)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True, null=True)

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
