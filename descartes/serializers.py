from rest_framework import serializers
from .models import Descartes

class DescartesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Descartes
        fields = '__all__'
