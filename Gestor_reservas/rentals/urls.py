from rest_framework import routers
from rentals import views
from django.urls import path, include

routers = routers.DefaultRouter()
routers.register(r'rentals', views.RentalsView, 'rentals')

urlpatterns = [
    path("GestorReservas/rentals/", include(routers.urls))
]