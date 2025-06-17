from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from . import views


urlpatterns = [
    path("", views.UserListCreateAPIView.as_view()),
    path("auth/", obtain_auth_token),
]