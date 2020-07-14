from django.db import models
from django.db.models import Model

# Create your models here.
class Cliente(Model):
    nombre = models.CharField(max_length = 15)
    apellido = models.CharField(max_length = 15)
    ciudad = models.CharField(max_length = 15)

    def Mostrar(self):
        cadena = "{0} {1}"
        return cadena.format(self.nombre, self.apellido)

    def __str__(self):
        return self.Mostrar()

class Producto(models.Model):
    Nombre = models.CharField(max_length = 50)
    descripcion = models.TextField(max_length = 999)
    imagen = models.ImageField(upload_to = "product")
    precio = models.DecimalField(max_digits = 5, decimal_places = 2)
    link = models.URLField(blank = True,null = True, max_length = 255)
    def __str__(self):
        return self.Nombre
