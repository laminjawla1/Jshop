from django.urls import path
from . import views


urlpatterns = [
    path("", views.CategoryMixin.as_view()),
    path("<int:pk>/", views.CategoryMixin.as_view()),
]