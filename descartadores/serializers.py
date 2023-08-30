from rest_framework import serializers
from .models import Descartadores

class DescartadoresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Descartadores
        fields = '__all__'
