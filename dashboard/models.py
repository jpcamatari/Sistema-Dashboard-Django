from django.db import models
import datetime

class Categoria(models.Model):
    categoria = models.CharField(max_length=50)

    def __str__(self):
        return self.categoria

class Movimento(models.Model):
    data = models.DateField(default=datetime.datetime.now())
    descricao = models.CharField(max_length=50)
    categoria = models.CharField(max_length=50)
    valor = models.FloatField()

    def __str__(self):
        return self.descricao

