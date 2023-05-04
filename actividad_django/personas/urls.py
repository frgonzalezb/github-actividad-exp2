from django.urls import path
from .views import listado_personas, persona_create, eliminar_personas

urlpatterns = [
    path("", listado_personas, name="listado_personas"),
    path('create/', persona_create, name='create'),
    path("<int:pk>/eliminar", eliminar_personas, name="eliminar_persona")
]
    
