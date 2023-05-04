from django.urls import path

from .views import persona_create

urlpatterns = [
    path('create/', persona_create, name='create'),
]
