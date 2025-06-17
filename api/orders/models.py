from django.db import models
from products.models import Product
from utils.base import BaseModel


class Order(BaseModel):
    products = models.ManyToManyField(Product)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    delivery_date = models.DateField()
