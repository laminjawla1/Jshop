from django.db import models
from utils.base import BaseModel
from users.models import User


class Brand(BaseModel):
    class Meta:
        ordering = ("name",)
    
    name = models.CharField(max_length=64, unique=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return str(self.name)
