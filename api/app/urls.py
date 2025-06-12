from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('brands/', include('brands.urls')),
    path('categories/', include('categories.urls')),
    path('orders/', include('orders.urls')),
    path('products/', include('products.urls')),
    path('users/', include('users.urls')),
]
