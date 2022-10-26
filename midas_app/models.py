from django.db import models

# Create your models here.


class Persona(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)


class PersonXML:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido