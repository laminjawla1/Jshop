from .views import ClientCreateAPIView, GlobalLoginAPIView
from django.urls import path
from django.contrib import admin
from .admin import tenant_admin_site


urlpatterns = [
    path("admin/", admin.site.urls),
    path("admin_tenants/", tenant_admin_site.urls),
    path("api/tenants/create/", ClientCreateAPIView.as_view()),
    path("api/users/login/", GlobalLoginAPIView.as_view())
]