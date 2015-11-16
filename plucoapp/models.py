from django.db import models

# Create your models here.

class Estudiante(models.Model):
	nombre = models.CharField (max_length=100, blank=True)
	dni = models.CharField (max_length=9, default='12345678A', primary_key=True)
	
	def __init__(self, nombre, dni):
		self.nombre = nombre
		self.dni = dni
		
	def __unicode__(self):
		return self.nombre	

class Profesor(models.Model):
	nombre = models.CharField (max_length=100, blank=True)
	dni = models.CharField (max_length=9, default='12345678A', primary_key=True)
	
	def __init__(self, nombre):
		self.nombre = nombre
	
	def __unicode__(self):
		return self.nombre
	
class Asignatura(models.Model):
	nombre = models.CharField (max_length=100, blank=True)
	nombre_id = models.CharField (max_length=30, default='nombre_id', primary_key=True)
	
	def __init__(self, nuevo):
		self.nombre = nuevo
	
	def __unicode__(self):
		return self.nombre
