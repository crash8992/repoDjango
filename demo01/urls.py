from django.contrib import admin
from django.urls import path, include  # <--- ¡OJO AQUÍ! Agrega ", include"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('web01.urls')),
]