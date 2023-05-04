from django.urls import path
from .views import listado_personas, persona_create

urlpatterns = [
    path("", listado_personas, name="listado_personas"),
    path('create/', persona_create, name='create'),
]
    
