from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import hola, product_list, login_user, private_endpoint, logout_user, endpoint_venta

router = DefaultRouter()

urlpatterns = [
    path("saludo/", hola, name="saludo"),
    path("productos/", product_list, name='product_list'),
    path("login/", login_user, name="login-user"),
    path("logout/", logout_user, name="logout-user"),
    path("private/", private_endpoint, name="private-endpoint"),
    path("venta/", endpoint_venta, name="endpoint venta"),
]