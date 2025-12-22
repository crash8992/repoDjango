from django.urls import path
from . import views

urlpatterns = [
    # Ruta vacía = página de inicio
    path('', views.index, name='inicio'),
]