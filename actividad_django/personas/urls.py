from django.urls import path
from .views import listado_personas, eliminar_personas
urlpatterns = [
    path("", listado_personas, name="listado_personas"),
    path("<int:pk>/eliminar", eliminar_personas, name="eliminar_persona")
]
