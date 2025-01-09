from rest_framework import viewsets
from .serializers import RentalsSerializer
from .models import Rentals

class RentalsView(viewsets.ModelViewSet):
    serializer_class = RentalsSerializer
    queryset = Rentals.objects.all()
