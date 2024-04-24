from .models import viviendas, empleados
from rest_framework import serializers

class ViviendaSerializer(serializers.ModelSerializer):
    class Meta:
        model = viviendas
        fields = '__all__'
        
class EmpleadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = empleados
        fields = '__all__'