from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import generics, status
#from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import RetrieveUpdateDestroyAPIView

from .models import Ecopontos
from .serializers import EcopontosSerializer

class EcopontosListCreateView(generics.ListCreateAPIView):
    queryset = Ecopontos.objects.all()
    serializer_class = EcopontosSerializer
    #permission_classes = [IsAuthenticated]

class EcopontosRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Ecopontos.objects.all()
    serializer_class = EcopontosSerializer
    #permission_classes = [IsAuthenticated]

@api_view(['POST'])
#@permission_classes([IsAuthenticated])
def create_ecoponto(request):
    serializer = EcopontosSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
#@permission_classes([IsAuthenticated])
def ecopontos_detail(request, pk):
    try:
        ecoponto = Ecopontos.objects.get(pk=pk)
    except Ecopontos.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = EcopontosSerializer(ecoponto)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = EcopontosSerializer(ecoponto, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        ecoponto.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
