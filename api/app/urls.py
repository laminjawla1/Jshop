from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path("auth/", obtain_auth_token),
    path('admin/', admin.site.urls),
    path('brands/', include('brands.urls')),
    path('categories/', include('categories.urls')),
    path('orders/', include('orders.urls')),
    path('products/', include('products.urls')),
    path('users/', include('users.urls')),
]
