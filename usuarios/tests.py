from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from .models import Usuarios
from ecopontos.models import Ecopontos

class UsuariosTests(APITestCase):
    def setUp(self):
        self.ecoponto = Ecopontos.objects.create(nome='Ecoponto Teste')
        self.usuario_data = {
            'nome': 'Usuário de Teste',
            'cpf': '12345678901',
            'email': 'usuario@teste.com',
            'cargo': 'Analista',
            'ecoponto': self.ecoponto,
        }
        self.usuario = Usuarios.objects.create(**self.usuario_data)
        self.url = reverse('usuarios-list')

    def test_list_usuarios(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_usuario(self):
        data = {
            'nome': 'Novo Usuário',
            'cpf': '98765432109',
            'email': 'novo_usuario@example.com',
            'cargo': 'Gerente',
            'ecoponto': self.ecoponto.id,
        }
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_retrieve_usuario(self):
        url = reverse('usuarios-detail', args=[self.usuario.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_usuario(self):
        url = reverse('usuarios-detail', args=[self.usuario.id])
        data = {
            'nome': 'Nome Atualizado',
            'cpf': '12345678901',
            'email': 'usuario@example.com',
            'cargo': 'Analista Sênior',
            'ecoponto': self.ecoponto.id,
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_usuario(self):
        url = reverse('usuarios-detail', args=[self.usuario.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
