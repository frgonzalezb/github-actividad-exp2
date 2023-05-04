from django.urls import path
from .views import listado_personas, persona_create, eliminar_personas, editar_persona

urlpatterns = [
    path("", listado_personas, name="listado_personas"),
    path('create/', persona_create, name='create'),
    path("<int:pk>/eliminar", eliminar_personas, name="eliminar_persona"),
    path("<int:pk>/editar", editar_persona, name="editar_persona")
]
    
