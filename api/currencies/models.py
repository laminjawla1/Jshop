from django.db import models
from utils.base import BaseModel


class Currency(BaseModel):
    class Meta:
        verbose_name_plural = "Currencies"

    code = models.CharField(max_length=3, unique=True)
    name = models.CharField(max_length=50, unique=True)
    symbol = models.CharField(max_length=5, unique=True)
    is_active = models.BooleanField(default=True)

    def __str__(self) -> str:
        return f"{self.name}({self.code} | ({self.symbol}))"
