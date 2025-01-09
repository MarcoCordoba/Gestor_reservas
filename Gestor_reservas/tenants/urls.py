from rest_framework import routers
from tenants import views
from django.urls import path, include

routers = routers.DefaultRouter()
routers.register(r'tenants', views.TenantsView, 'tenants')

urlpatterns = [
    path("GestorReservas/tenants/", include(routers.urls))
]

