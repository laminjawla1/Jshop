from django.db import models
from utils.base import BaseModel
from users.models import User


class Location(BaseModel):
    class Meta:
        ordering = ("name",)

    name = models.CharField(max_length=64)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self) -> str:
        return f"{self.name} -> [{self.latitude}, {self.longitude}] | {self.owner}"
