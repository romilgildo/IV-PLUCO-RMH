from django.contrib import admin
from plucoapp.models import Estudiante, Profesor, Asignatura

# Register your models here.

admin.site.register(Estudiante)
admin.site.register(Profesor)
admin.site.register(Asignatura)
