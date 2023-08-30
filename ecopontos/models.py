from django.db import models

class Ecopontos(models.Model):
    cep = models.CharField(default='-', max_length=20)
    bairro = models.CharField(default='-', max_length=20)
    endereco = models.CharField(default='-', max_length=30)
    situacao = models.CharField(default='-', max_length=10)

    def __str__(self):
        return self.endereco
