from django import forms

from .models import Persona


class PersonaCreate(forms.ModelForm):
    class Meta:
        model = Persona
        fields = '__all__'

    rut = forms.CharField(label="RUT", max_length=13)
    nombre = forms.CharField(label="Nombre", max_length=50)
    apellido = forms.CharField(label="Apellido", max_length=50)


