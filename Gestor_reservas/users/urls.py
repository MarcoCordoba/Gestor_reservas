from rest_framework import routers
from users import views
from django.urls import path, include

routers = routers.DefaultRouter()
routers.register(r'users', views.UsersView, 'users')

urlpatterns = [
    path("GestorReservas/users/", include(routers.urls))
]
