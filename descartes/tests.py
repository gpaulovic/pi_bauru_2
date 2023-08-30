from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Descartes, Descartadores
from .serializers import DescartesSerializer

class DescartesTests(TestCase):
    def setUp(self):
        self.client = APIClient()

        # Criar um objeto descartador
        self.descartador_data = {
            'nome': 'descartador Teste',
        }
        self.descartador = Descartadores.objects.create(**self.descartador_data)

        # Criar um objeto Descartes referenciando o objeto descartador
        self.descarte_data = {
            'descartador': self.descartador,
            'nome': 'Descarte Teste',
            'tipo': 'Tipo Teste',
            'quantidade': 10,
        }
        self.descarte = Descartes.objects.create(**self.descarte_data)

    def test_list_descartes(self):
        response = self.client.get(reverse('descartes:home-descartes'))
        descarte = Descartes.objects.all()
        serializer = DescartesSerializer(descarte, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_descarte(self):
        new_descarte_data = {
            'descartador': self.descartador,
            'nome': 'Novo Descarte',
            'tipo': 'Novo Tipo',
            'quantidade': 5,
        }
        response = self.client.post(reverse('descartes:save-descartes'), new_descarte_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


    def test_retrieve_descarte(self):
        response = self.client.get(reverse('descartes:editar-descartes', kwargs={'pk': self.descarte.pk}))
        descarte = Descartes.objects.get(pk=self.descarte.pk)
        serializer = DescartesSerializer(descarte)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_descarte(self):
        updated_data = {
            'descartador': self.descartador.pk,  # Usar a chave primária do objeto descartador
            'nome': 'Novo Nome',
            'tipo': 'Novo Tipo',
            'quantidade': 20,
        }
        response = self.client.put(reverse('descartes:update-descartes', kwargs={'pk': self.descarte.pk}), updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_descarte(self):
        response = self.client.delete(reverse('descartes:delete-descartes', kwargs={'pk': self.descarte.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Descartes.objects.filter(pk=self.descartes.pk).exists())
