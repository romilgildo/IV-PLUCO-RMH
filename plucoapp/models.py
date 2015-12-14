from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Usuario(models.Model):
	OPCIONES = (
		('ESTUDIANTE', 'Estudiante'),
		('PROFESOR', 'Profesor')
	)
	nick = models.ForeignKey(User, blank=True, null=True)
	nombre = models.CharField(max_length=100, blank=True)
	email = models.EmailField(blank=True, unique= True, primary_key=True)
	tipo = models.CharField(max_length=10, choices=OPCIONES, default="ESTUDIANTE")
	
	def __init__(self, nombre, email, tipo):
		self.nombre = nombre
		self.email = email
		self.tipo = tipo
	
	def __unicode__(self):
		return self.nombre
	
class Asignatura(models.Model):
	nombre = models.CharField (max_length=100, blank=True)
	nombre_id = models.CharField (max_length=30, default='nombre_id', primary_key=True)
	
	def __init__(self, nuevo):
		self.nombre = nuevo
	
	def __unicode__(self):
		return self.nombre
