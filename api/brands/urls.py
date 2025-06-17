from django.urls import path
from . import views


urlpatterns = [
    path("", views.BrandListCreateAPIView.as_view()),
    # path("", views.BrandMixin.as_view()),
    # path("<int:pk>/", views.BrandRetrieveUpdateDestroyAPIView.as_view()),
    path("<int:pk>/", views.BrandMixin.as_view()),
]