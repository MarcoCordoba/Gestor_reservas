from rest_framework import serializers
from .models import Tenants

class TenantsSerializer(serializers.ModelSerializer):
    class meta:
        model = Tenants
        fields  = '__all__'
        