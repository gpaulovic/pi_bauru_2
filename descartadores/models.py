from django.db import models


class Descartadores(models.Model):
    nome = models.CharField(default='-', max_length=30)
    documento = models.IntegerField(primary_key=True)
    email = models.CharField(default='-', max_length=20)
    endereco = models.CharField(default='-', max_length=30)

    def __str__(self):
        return self.nome
