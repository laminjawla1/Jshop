from django.urls import path
from . import views


urlpatterns = [
    path("", views.CurrencyMixin.as_view()),
    path("<int:pk>/", views.CurrencyMixin.as_view()),
]