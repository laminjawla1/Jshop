from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from . import views


urlpatterns = [
    path("", views.UserMixin.as_view()),
    path("<int:pk>/", views.UserMixin.as_view()),
    path("login/", obtain_auth_token),
]