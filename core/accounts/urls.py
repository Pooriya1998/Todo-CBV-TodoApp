from django.urls import path
from .views import Login_View, Register_View, Logout_View

app_name = "accounts"

urlpatterns = [
    path("login/", Login_View.as_view(), name="login"),
    path("logout", Logout_View.as_view(), name="logout"),
    path("register/", Register_View.as_view(), name="register"),
]