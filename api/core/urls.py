from .views import ClientCreateAPIView, GlobalLoginAPIView
from django.urls import path, include
from django.contrib import admin


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/tenants/create/", ClientCreateAPIView.as_view()),
    path("api/users/login/", GlobalLoginAPIView.as_view()),
    path('api/units/', include('units.urls')),
    path('api/currencies/', include('currencies.urls')),
]