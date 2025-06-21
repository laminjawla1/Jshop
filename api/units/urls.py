from django.urls import path
from . import views


urlpatterns = [
    path("", views.UnitMixin.as_view()),
    path("<int:pk>/", views.UnitMixin.as_view()),
]