from django.db import models

# Create your models here.
class Producto(models.Model):
    nombre = models.CharField(max_length=40)
    categoria = models.CharField(max_length=8)
    precio = models.CharField(max_length=10)

    def __str__(self):
        return self.nombre