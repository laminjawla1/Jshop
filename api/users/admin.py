from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm
from .models import User

class CustomUserChangeForm(UserChangeForm):
    """Ensure custom fields, including image, are displayed in Django Admin."""
    class Meta:
        model = User
        fields = "__all__"


class CustomUserAdmin(UserAdmin):
    form = CustomUserChangeForm
    model = User

    # Add custom fields to the admin form
    fieldsets = (
        *UserAdmin.fieldsets,  # Retain default UserAdmin fields
    )

admin.site.register(User, CustomUserAdmin)
