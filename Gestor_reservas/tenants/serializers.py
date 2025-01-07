from rest_framework import serializers
from .models import Tenant

class TenantSerializer(serializers.ModelSerializer):
    class meta:
        model = 'Tenant'
        fields  = '__all__'
        