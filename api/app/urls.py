from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('api/brands/', include('brands.urls')),
    path('api/categories/', include('categories.urls')),
    path('api/orders/', include('orders.urls')),
    path('api/products/', include('products.urls')),
    path('api/locations/', include('locations.urls')),
    path('api/users/', include('users.urls')),
    path('api/units/', include('units.urls')),
    path('api/currencies/', include('currencies.urls')),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
