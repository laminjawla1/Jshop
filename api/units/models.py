from django.db import models
from utils.base import BaseModel


class Unit(BaseModel):
    name = models.CharField(max_length=20, unique=True)
    symbol = models.CharField(max_length=10)

    def __str__(self) -> str:
        return f"{self.name}({self.symbol})"
