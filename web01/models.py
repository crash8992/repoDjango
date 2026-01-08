from django.db import models

class Tarea(models.Model):
    titulo = models.CharField(max_length=200)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    completada = models.BooleanField(default=False)

    def __str__(self):
        return self.titulo
