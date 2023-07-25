from django import forms
from . import models


class ContactoForm(forms.ModelForm):

    class Meta:
        model = models.Contacto
        fields = ['nombre_apellido', 'email', 'asunto', 'mensaje']

        widgets = {
            'nombre_apellido': forms.TextInput(attrs={'class': 'form-control'}),
            'asunto': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'mensaje': forms.Textarea(attrs={'class': 'form-control'}),
        }