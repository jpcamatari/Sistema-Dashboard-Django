from django.db import models

class Movimento(models.Model):
    data = models.DateTimeField()
    descricao = models.CharField(max_length=50)
    categoria = models.CharField(max_length=50)
    valor = models.FloatField()

    def __str__(self):
        return self.data