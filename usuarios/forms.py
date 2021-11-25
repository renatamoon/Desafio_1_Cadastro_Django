from django import forms
from django.forms import widgets, DateInput
from .models import Usuario

class UsuarioForms(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nome', 'data_nascimento', 'login', 'senha']

        widgets = {
            'data_nascimento': DateInput(
                attrs={'type': "date"}
            )
        }