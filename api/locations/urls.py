from django.urls import path
from . import views


urlpatterns = [
    path("", views.LocationMixin.as_view()),
    path("<int:pk>/", views.LocationMixin.as_view()),
]