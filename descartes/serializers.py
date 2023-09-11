from rest_framework import serializers
from .models import Descartes
from descartadores.serializers import DescartadoresSerializer  
class DescartesSerializer(serializers.ModelSerializer):
    
    descartador = DescartadoresSerializer()

    class Meta:
        model = Descartes
        fields = '__all__'
