from django.db import models
from django.db.models import Model

# Create your models here.
class Cliente(Model):
    nombre = models.CharField(max_length = 15)
    apellido = models.CharField(max_length = 15)
    ciudad = models.CharField(max_length = 15)

    def Mostra(self):
        mostrar = {'0','1'}
        return self.nombre

class Producto(Model):
    Nombre = models.CharField(max_length = 10)
    descripcion = models.TextField(max_length = 10)
    imagen = models.ImageField()
    precio = models.DecimalField(max_digits = 5, decimal_places = 2)
