from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Descartes, Descartadores
from .serializers import DescartesSerializer, DescartadoresSerializer

class DescartesTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.descartadores_data = {
            'nome': 'Nome Descartador',
            'documento': '12345678901',
            'email': 'email@example.com',
            'endereco': 'Endereço Teste',
        }
        self.descartador = Descartadores.objects.create(**self.descartadores_data)

        self.descartes_data = {
            'descartador': self.descartador,
            'nome': 'Nome Descarte',
            'tipo': 'Tipo Descarte',
            'quantidade': 5,
        }
        self.descarte = Descartes.objects.create(**self.descartes_data)

    def test_list_descartes(self):
        response = self.client.get(reverse('descartes:home-descartes'))
        descartes = Descartes.objects.all()
        serializer = DescartesSerializer(descartes, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_descarte(self):
        response = self.client.post(reverse('descartes:home-descartes'), self.descartes_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_retrieve_descarte(self):
        response = self.client.get(reverse('descartes:editar-descartes', kwargs={'pk': self.descarte.pk}))
        serializer = DescartesSerializer(self.descarte)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_descarte(self):
        updated_data = {
            'descartador': self.descartador.pk,
            'nome': 'Novo Nome Descarte',
            'tipo': 'Novo Tipo Descarte',
            'quantidade': 10,
        }
        response = self.client.put(reverse('descartes:editar-descartes', kwargs={'pk': self.descarte.pk}), updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_descarte(self):
        response = self.client.delete(reverse('descartes:delete-descartes', kwargs={'id': self.descarte.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Descartes.objects.filter(pk=self.descarte.pk).exists())
