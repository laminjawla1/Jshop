from django.urls import path
from .import views


urlpatterns = [
    path("", views.products),
    path("<int:product_id>/", views.get_product)
]