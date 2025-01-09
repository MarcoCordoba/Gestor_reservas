from rest_framework import viewsets
from .serializers import PropertiesSerializer
from .models import Properties

# Create your views here.

class PropertiesView(viewsets.ModelViewSet):
    serializer_class = PropertiesSerializer
    queryset = Properties.objects.all()