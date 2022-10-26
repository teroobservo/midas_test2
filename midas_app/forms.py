from django import forms
from .models import Persona


class PersonaForm(forms.ModelForm):
    nombre = forms.CharField(label='Nombre', max_length=100, required=True,
                            widget=forms.TextInput(
                                attrs={'class': 'form-control',
                                       'placeholder': 'Nombre'}
                            ))
    apellido = forms.CharField(label='Apellido', max_length=100, required=True,
                             widget=forms.TextInput(
                                 attrs={'class': 'form-control',
                                        'placeholder': 'Apellido'}
                             ))

    class Meta:
        model = Persona
        fields = [
            'nombre',
            'apellido',
        ]