from rest_framework import serializers
from .models import Propertie


class PropertieSerializer(serializers.ModelSerializer):
    class meta:
        model = 'Propertie'
        fields  = '__all__'