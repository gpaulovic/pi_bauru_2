from django.db import models


class Descartadores(models.Model):
    nome = models.CharField(default='-', max_length=30)
    documento = models.CharField(primary_key=True, max_length=14)
    email = models.CharField(default='-', max_length=20)
    endereco = models.CharField(default='-', max_length=30)

    def __str__(self):
        return self.nome
