from socket import fromshare
from django import forms

class formularioLancar(forms.Form):
    data = forms.DateField()
    descricao = forms.CharField(max_length=50)
    categoria = forms.CharField(max_length=50)
    valor = forms.FloatField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['data'].widget.attrs['class'] = 'form-control mb-3 date'
        self.fields['data'].widget.attrs['placeholder'] = 'Digite uma data...'
        self.fields['descricao'].widget.attrs['class'] = 'form-control mb-3'
        self.fields['categoria'].widget.attrs['class'] = 'form-control mb-3'
        self.fields['valor'].widget.attrs['class'] = 'form-control mb-3'