from django.db import models
from ecopontos.models import Ecopontos

class Usuarios(models.Model):
    nome = models.CharField(default='-', max_length=30)
    cpf = models.CharField(default='-', max_length=15)
    email = models.CharField(default='-', max_length=30)
    cargo = models.CharField(default='-', max_length=30)
    ecoponto = models.ForeignKey(Ecopontos, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome
