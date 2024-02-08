from rest_framework import serializers
from .models import tipo_cotizacion_riego
 
class tipo_cotizacion_riegoSerializer(serializers.ModelSerializer):
    class Meta:
        model = tipo_cotizacion_riego
        fields = '__all__'