from django.urls import path, include
from rest_framework import routers
from properties import views


routers =  routers.DefaultRouter()
routers.register(r'properties', views.PropertiesView, 'properties')

urlpatterns = [
    path("GestorReservas/properties/", include(routers.urls))
]
