from django.shortcuts import render
from .models import Persona
# Create your views here.
def listado_personas(request):
    personas = Persona.objects.all()
    return render(request, 'personas/listado_personas.html', {'personas': personas})
