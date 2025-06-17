from django.db import models
from utils.base import BaseModel


class Category(BaseModel):
    class Meta:
        verbose_name_plural = "Categories"
        ordering = ("name",)

    name = models.CharField(max_length=32, unique=True)

    def __str__(self) -> str:
        return str(self.name)
