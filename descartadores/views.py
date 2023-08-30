from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .models import Descartadores
from .serializers import DescartadoresSerializer
from rest_framework.decorators import api_view


class DescartadoresListCreateView(generics.ListCreateAPIView):
    queryset = Descartadores.objects.all()
    serializer_class = DescartadoresSerializer

class DescartadoresRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Descartadores.objects.all()
    serializer_class = DescartadoresSerializer


@api_view(['GET', 'POST'])
def descartadores_list(request):
    if request.method == 'GET':
        descartadores = Descartadores.objects.all()
        serializer = DescartadoresSerializer(descartadores, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = DescartadoresSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def descartadores_detail(request, documento):
    try:
        descartador = Descartadores.objects.get(documento=documento)
    except Descartadores.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = DescartadoresSerializer(descartador)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = DescartadoresSerializer(descartador, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        descartador.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
