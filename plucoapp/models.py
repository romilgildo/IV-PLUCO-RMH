from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Usuario(models.Model):
	OPCIONES = (
		('ESTUDIANTE', 'Estudiante'),
		('PROFESOR', 'Profesor')
	)
	nick = models.ForeignKey(User, null=True)
	nombre = models.CharField(max_length=100)
	email = models.EmailField(primary_key=True)
	tipo = models.CharField(max_length=10, choices=OPCIONES, default="ESTUDIANTE")
	
	def __unicode__(self):
		return self.nombre
	
class Asignatura(models.Model):
	nombre = models.CharField (max_length=100)
	nombre_id = models.CharField (max_length=30, default='nombre_id', primary_key=True)
	
	def __unicode__(self):
		return self.nombre
