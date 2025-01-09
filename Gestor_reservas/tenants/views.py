from rest_framework import viewsets
from .serializers import TenantsSerializer
from .models import Tenants

class TenantsView(viewsets.ModelViewSet):
    serializer_class = TenantsSerializer
    queryset = Tenants.objects.all()