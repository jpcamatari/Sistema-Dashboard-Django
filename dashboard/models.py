from django.db import models
import datetime

#Modelagem da tabela Categoria
class Categoria(models.Model):
    categoria = models.CharField(max_length=50)
    def __str__(self):
        return self.categoria

#Modelagem da tabela movimento, resposavel por receber todos os inserts feitos pelo formulario no banco de dados
class Movimento(models.Model):
    data = models.DateField(default=datetime.datetime.now())
    descricao = models.CharField(max_length=50)
    categoria = models.CharField(max_length=50)
    valor = models.FloatField()
    def __str__(self):
        return self.descricao

