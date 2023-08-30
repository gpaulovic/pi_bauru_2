from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Descartes
from .serializers import DescartesSerializer

class DescartesListCreateView(generics.ListCreateAPIView):
    queryset = Descartes.objects.all()
    serializer_class = DescartesSerializer

class DescartesRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Descartes.objects.all()
    serializer_class = DescartesSerializer

@api_view(['POST'])
def save(request):
    serializer = DescartesSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def update(request, id):
    try:
        descarte = Descartes.objects.get(id=id)
    except Descartes.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    serializer = DescartesSerializer(descarte, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete(request, id):
    try:
        descarte = Descartes.objects.get(id=id)
    except Descartes.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    descarte.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
