from django.urls import path
from . import views


urlpatterns = [
    path("", views.BrandMixin.as_view()),
    path("<int:pk>/", views.BrandMixin.as_view()),
]