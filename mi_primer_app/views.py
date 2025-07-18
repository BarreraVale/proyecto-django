from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Familiar

def saludo(request):
    return HttpResponse("¡Hola, mundo!")  # Respuesta simple de texto plano



def saludo_con_template(request):
    return render(request, 'mi_primer_app/saludo.html')  # Renderiza un template HTML

def crear_familiar(request, nombre):
    if nombre is not None:
        nuevo_familiar = Familiar(
            nombre=nombre,
            apellidos="Apellido",
            edad=27,
            fecha_nacimiento="1997-07-21",
            parentesco="Primo"
        )
        nuevo_familiar.save()
    return render(request, 'mi_primer_app/crear_familiar.html', {'nombre': nombre})