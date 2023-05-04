from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

from .forms import PersonaCreate


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
