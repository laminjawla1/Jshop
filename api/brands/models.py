from django.db import models
from utils.base import BaseModel


class Brand(BaseModel):
    class Meta:
        ordering = ("name",)
    
    name = models.CharField(max_length=64, unique=True)

    def __str__(self) -> str:
        return str(self.name)
