from django.urls import path
from .views import saludo
from .views import saludo_con_template
from .views import crear_familiar

urlpatterns = [
    path('Hola-mundo/', saludo),
    path('Hola-mundo-template/', saludo_con_template),
    path("crear-familiar/<str:nombre>/", crear_familiar)
]
