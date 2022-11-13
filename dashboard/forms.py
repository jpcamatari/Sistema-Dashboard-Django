from dataclasses import fields
from django import forms
from .models import Movimento

class formularioLancar(forms.ModelForm):
    class Meta:
        model = Movimento
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['data'].widget.attrs['class'] = 'form-control mb-3 date'
        self.fields['data'].error_messages['required'] = ""
        self.fields['descricao'].widget.attrs['class'] = 'form-control mb-3'
        self.fields['descricao'].error_messages['required'] = ""
        self.fields['categoria'].widget.attrs['class'] = 'form-control mb-3'
        self.fields['categoria'].error_messages['required'] = ""
        self.fields['valor'].widget.attrs['class'] = 'form-control mb-3'
        self.fields['valor'].error_messages['required'] = ""
        