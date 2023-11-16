from django.db import models

# Create your models here.
class Peliculas(models.Model):
    nombre = models.CharField(max_length=64)
    puntaje = models.IntegerField()
    def __str__(self):
        return f"{self.nombre},{self.puntaje}"
    
class Series(models.Model):
    nombre = models.CharField(max_length=64)
    puntaje = models.IntegerField()
    def __str__(self):
        return f"{self.nombre},{self.puntaje}"
    
class Actores(models.Model):
    nombre = models.CharField(max_length=64)
    puntaje = models.IntegerField()
    def __str__(self):
        return f"{self.nombre},{self.puntaje}"

