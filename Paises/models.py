from django.db import models

# Create your models here.

class Pais(models.Model):
    Codigo = models.CharField(max_length = 3)
    Nombre = models.CharField(max_length = 70)
    Continente = models.CharField(max_length = 65)
    Region = models.CharField(max_length = 70)
    Area = models.DecimalField(max_digits = 30, decimal_places = 2)
    Independence = models.IntegerField(default = 1500)

    def __str__(self):
        return self.Nombre


class Ciudad(models.Model):
    Ciudad_pais = models.ForeignKey(Pais)
    Nombre_Ciudad = models. CharField(max_length = 70)
    Distrito = models.CharField(max_length = 60)
    Poblacion = models.IntegerField(default = 0)

    def __str__(self):
        return self.Nombre_Ciudad


class Lenguaje(models.Model):
    Lenguaje_Pais = models.ForeignKey(Pais)
    Lenguaje = models.CharField(max_length = 70)

    def __str__(self):
        return self.Lenguaje

