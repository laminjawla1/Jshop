from django.db import models
from django_tenants.models import TenantMixin, DomainMixin
from utils.constants import HOW_DID_YOU_HEAR_CHOICES
from phonenumber_field.modelfields import (
    PhoneNumberField,
)


class Client(TenantMixin):
    # Business Personal Details
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to="business_logos/", blank=True, null=True)
    domain_name = models.CharField(max_length=100)

    # Business Contact Details
    website = models.URLField(blank=True, null=True)
    phone_number = PhoneNumberField(blank=True, null=True)
    contact_person = models.CharField(max_length=255)
    contact_email = models.EmailField()

    # Business Compliance / KYC
    heard_from = models.CharField(
        max_length=20,
        choices=HOW_DID_YOU_HEAR_CHOICES,
        default="other",
        verbose_name="How did you hear about us?"
    )
    agreed_to_terms = models.BooleanField(
        default=False,
        help_text="I agree to the General Terms of Use, Merchant Terms of Use & General Privacy Policy of Jshop"
    )
    wants_marketing = models.BooleanField(
        default=False,
        help_text="I'd like to receive marketing communication and business tips from Jshop"
    )

    weekly_orders = models.PositiveIntegerField(
        help_text="How many orders do you get weekly?",
        verbose_name="Weekly Orders"
    )
    staff_count = models.PositiveIntegerField(
        help_text="How many staff do you have?",
        verbose_name="Number of Staff"
    )
    physical_store_count = models.PositiveIntegerField(
        help_text="How many physical stores do you have?",
        verbose_name="Number of Physical Stores"
    )

    created_on = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


class Domain(DomainMixin):
    pass