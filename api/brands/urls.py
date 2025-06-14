from django.urls import path
from . import views


urlpatterns = [
    path("", views.brands),
    path("<int:brand_id>", views.brand),
]