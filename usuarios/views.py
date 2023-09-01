from rest_framework import generics, viewsets, status
from rest_framework.response import Response
from .models import Usuarios
from .serializers import UsuariosSerializer
from django.shortcuts import get_object_or_404

class UsuariosListView(generics.ListCreateAPIView):
    queryset = Usuarios.objects.all()
    serializer_class = UsuariosSerializer

class UsuariosDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Usuarios.objects.all()
    serializer_class = UsuariosSerializer

    def perform_update(self, serializer):
        serializer.save()

    def perform_destroy(self, instance):
        instance.delete()
