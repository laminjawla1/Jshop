from django.db import models
from utils.base import BaseModel
from users.models import User


class Category(BaseModel):
    class Meta:
        verbose_name_plural = "Categories"
        ordering = ("name",)

    name = models.CharField(max_length=32, unique=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return str(self.name)
