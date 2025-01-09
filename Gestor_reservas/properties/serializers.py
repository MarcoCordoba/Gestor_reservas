from rest_framework import serializers
from .models import Properties


class PropertiesSerializer(serializers.ModelSerializer):
    class meta:
        model = Properties
        fields  = '__all__'