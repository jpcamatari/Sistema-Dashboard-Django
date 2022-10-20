from django.db import models

class Categoria(models.Model):
    categoria = models.CharField(max_length=50)

    def __str__(self):
        return self.categoria

class Movimento(models.Model):
    data = models.DateTimeField()
    descricao = models.CharField(max_length=50)
    categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING)
    valor = models.FloatField()

    def __str__(self):
        return self.data

