from django.urls import path
from .import views


urlpatterns = [
    path("", views.ProductMixin.as_view()),
    path("<int:product_id>/", views.ProductMixin.as_view())
]