from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Descartes, Descartadores
from .serializers import DescartesSerializer

class DescartesTests(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_list_descartes(self):
        descartador_data = {
            'nome': 'descartador Teste',
        }
        descartador = Descartadores.objects.create(**descartador_data)

        descarte_data = {
            'descartador': descartador,
            'nome': 'Descarte Teste',
            'tipo': 'Tipo Teste',
            'quantidade': 10,
        }
        descarte = Descartes.objects.create(**descarte_data)

        response = self.client.get(reverse('descartes:home-descartes'))
        serializer = DescartesSerializer([descarte], many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_descarte(self):
        descartador_data = {
            'nome': 'descartador Teste',
        }
        descartador = Descartadores.objects.create(**descartador_data)

        new_descarte_data = {
            'descartador': descartador.pk,
            'nome': 'Novo Descarte',
            'tipo': 'Novo Tipo',
            'quantidade': 5,
        }
        response = self.client.post(reverse('descartes:save-descartes'), new_descarte_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_retrieve_descarte(self):
        descartador_data = {
            'nome': 'descartador Teste',
        }
        descartador = Descartadores.objects.create(**descartador_data)

        descarte_data = {
            'descartador': descartador,
            'nome': 'Descarte Teste',
            'tipo': 'Tipo Teste',
            'quantidade': 10,
        }
        descarte = Descartes.objects.create(**descarte_data)

        response = self.client.get(reverse('descartes:editar-descartes', kwargs={'pk': descarte.pk}))
        serializer = DescartesSerializer(descarte)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_descarte(self):
        descartador_data = {
            'nome': 'descartador Teste',
        }
        descartador = Descartadores.objects.create(**descartador_data)

        descarte_data = {
            'descartador': descartador,
            'nome': 'Descarte Teste',
            'tipo': 'Tipo Teste',
            'quantidade': 10,
        }
        descarte = Descartes.objects.create(**descarte_data)

        updated_data = {
            'descartador': descartador.pk,
            'nome': 'Novo Nome',
            'tipo': 'Novo Tipo',
            'quantidade': 20,
        }
        response = self.client.put(reverse('descartes:update-descartes', kwargs={'pk': descarte.pk}), updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_descarte(self):
        descartador_data = {
            'nome': 'descartador Teste',
        }
        descartador = Descartadores.objects.create(**descartador_data)

        descarte_data = {
            'descartador': descartador,
            'nome': 'Descarte Teste',
            'tipo': 'Tipo Teste',
            'quantidade': 10,
        }
        descarte = Descartes.objects.create(**descarte_data)

        response = self.client.delete(reverse('descartes:delete-descartes', kwargs={'pk': descarte.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Descartes.objects.filter(pk=descarte.pk).exists())
