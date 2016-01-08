from django.db import models
from django.contrib.auth.models import User

# Create your models here.
	
class Asignatura(models.Model):
	nombre = models.CharField (max_length=100)
	nombre_id = models.CharField (max_length=30, help_text="Nombre corto", primary_key=True)
	centro = models.CharField (max_length=100)
	titulacion = models.CharField (max_length=100)
	curso = models.CharField (max_length=1, help_text="Numero de curso")
	creador = models.CharField (max_length=100)
	web = models.URLField (default='http://www.ugr.es')
	
	def __unicode__(self):
		return self.nombre

class Usuario(models.Model):
	OPCIONES = (
		('ESTUDIANTE', 'Estudiante'),
		('PROFESOR', 'Profesor')
	)
	nick = models.OneToOneField(User, primary_key=True)
	nombre = models.CharField(max_length=100)
	email = models.EmailField()
	tipo = models.CharField(max_length=10, choices=OPCIONES, default="ESTUDIANTE")
	asignaturas = models.ManyToManyField(Asignatura)
	imagen = models.ImageField(upload_to='perfiles/', blank=True)
	
	def __unicode__(self):
		return self.nombre
