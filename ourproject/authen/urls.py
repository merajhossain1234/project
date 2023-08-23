from django.urls import path
from .import views

urlpatterns = [
    path("signup/", views.SignupAPIView.as_view(), name="user-signup"),
    path("login/", views.LoginAPIView.as_view(), name="user-login"),
    path("logout/", views.LogoutAPIView.as_view(), name="user-logout")
]
