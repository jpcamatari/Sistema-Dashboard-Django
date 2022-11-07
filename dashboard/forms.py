from socket import fromshare
from django import forms

class formularioLancar(forms.Form):
    data = forms.DateField()
    descricao = forms.CharField(max_length=50)
    categoria = forms.CharField(max_length=50)
    valor = forms.FloatField()