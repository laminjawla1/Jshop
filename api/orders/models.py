from django.db import models
from products.models import Product
from users.models import User
from utils.base import BaseModel


class Order(BaseModel):
    products = models.ManyToManyField(Product)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    delivery_date = models.DateField()
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
