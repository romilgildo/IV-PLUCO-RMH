from django.db import models

# Create your models here.

class Estudiante(models.Model):
	nombre = models.CharField (max_length=200)
	
	def __init__(self, nuevo):
		self.nombre = nuevo
		
	def __unicode__(self):
		return self.nombre	

class Profesor(models.Model):
	nombre = models.CharField (max_length=200)
	
	def __init__(self, nuevo):
		self.nombre = nuevo
	
	def __unicode__(self):
		return self.nombre
	
class Asignatura(models.Model):
	nombre = models.CharField (max_length=200)
	
	def __init__(self, nuevo):
		self.nombre = nuevo
	
	def __unicode__(self):
		return self.nombre
