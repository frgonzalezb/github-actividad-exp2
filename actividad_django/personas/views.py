from django.shortcuts import render, redirect, get_object_or_404
from .models import Persona
# Create your views here.
def listado_personas(request):
    personas = Persona.objects.all()
    return render(request, 'personas/listado_personas.html', {'personas': personas})


def eliminar_personas(request, pk):
    persona = get_object_or_404(Persona, pk=pk)
    if request.method == 'POST':
        persona.delete()
        return redirect('listado_personas')
