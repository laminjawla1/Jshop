from .views import index
from django.urls import path
from django.contrib import admin
from .admin import tenant_admin_site


urlpatterns = [
    path("admin/", admin.site.urls),
    path("admin_tenants/", tenant_admin_site.urls),

]