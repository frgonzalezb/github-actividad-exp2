from django.shortcuts import render, redirect, get_object_or_404
from .models import Persona
from django.shortcuts import render, redirect

from .forms import PersonaCreate

# Create your views here.
def listado_personas(request):
    personas = Persona.objects.all()
    return render(request, 'personas/listado_personas.html', {'personas': personas})


def persona_create(request):
    # if this is a POST request we need to process the form data
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = PersonaCreate(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            form.save()
            return redirect("listado_personas")

    # if a GET (or any other method) we'll create a blank form
    else:
        form = PersonaCreate()

    return render(request, "personas/create.html", {"form": form})
def eliminar_personas(request, pk):
    persona = get_object_or_404(Persona, pk=pk)
    if request.method == 'POST':
        persona.delete()
        return redirect('listado_personas')


def editar_persona(request, pk):
    persona = get_object_or_404(Persona, pk=pk)
    if request.method == 'POST':
        form = PersonaCreate(request.POST, instance=persona)
        if form.is_valid():
            form.save()
            return redirect('listado_personas')
    else:
        form = PersonaCreate(instance=persona)
    return render(request, 'personas/editar_persona.html', {'form': form})