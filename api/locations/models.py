from django.db import models
from utils.base import BaseModel


class Location(BaseModel):
    class Meta:
        ordering = ("name",)

    name = models.CharField(max_length=64, unique=True)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.name} -> [{self.latitude}, {self.longitude}]"
