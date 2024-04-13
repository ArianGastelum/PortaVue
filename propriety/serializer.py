from .models import Login, ProprietyVivienda
from rest_framework import serializers

class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = Login
        fields = '__all__'

class ViviendaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProprietyVivienda
        fields = '__all__'