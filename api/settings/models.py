from django.db import models
from utils.base import BaseModel
from currencies.models import Currency


class Setting(BaseModel):
    default_currency = models.ForeignKey(Currency, on_delete=models.PROTECT, null=True)
    can_change_currency = models.BooleanField(default=False)
