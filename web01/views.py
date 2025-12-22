from django.shortcuts import render
import datetime # Importamos una librería de Python

def index(request):
    # Aquí sucede la magia del Backend
    fecha_actual = datetime.datetime.now().strftime("%d/%m/%Y %H:%M")
    
    # Preparamos el paquete de datos (Contexto)
    datos = {
        'nombre_estudiante': 'Cristian Bravo', 
        'curso': 'Desarrollo en Plataformas Web',
        'fecha': fecha_actual,
        'mensaje': 'todo funcionando en orden!'
    }
    
    # Enviamos los datos junto con la plantilla
    return render(request, 'web01/index.html', datos)