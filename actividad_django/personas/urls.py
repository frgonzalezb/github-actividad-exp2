from django.urls import path
from .views import listado_personas
urlpatterns = [
    path("", listado_personas, name="listado_personas")
]
