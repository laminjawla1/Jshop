from django.urls import path, include


urlpatterns = [
    path('api/brands/', include('brands.urls')),
    path('api/categories/', include('categories.urls')),
    path('api/orders/', include('orders.urls')),
    path('api/products/', include('products.urls')),
    path('api/users/', include('users.urls')),
]
