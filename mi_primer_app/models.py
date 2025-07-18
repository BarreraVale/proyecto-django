from django.db import models

# Create your models here.
class Familiar (models.Model):
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    edad = models.IntegerField()
    fecha_nacimiento = models.DateField()
    parentesco = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.nombre} {self.apellidos} ({self.parentesco}) - Edad: {self.edad} - Nacido el: {self.fecha_nacimiento}"