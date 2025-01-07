from rest_framework import serializers
from .models import Rental

class RentalSerializer(serializers.ModelSerializer):
    class meta:
        model = 'Rental'
        fields  = '__all__'