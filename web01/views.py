from django.shortcuts import render
# 1. IMPORTANTE: Importar tu modelo para poder usarlo
from .models import Tarea 

def index(request):

    lista_tareas = Tarea.objects.all()
    
    datos = {
        'curso': 'Desarrollo Web',
        'nombre_estudiante': 'Cristian Bravo',
        'tareas': lista_tareas  
    }
    
    return render(request, 'web01/index.html', datos)