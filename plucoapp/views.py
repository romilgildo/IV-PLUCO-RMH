from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from .models import Asignatura, Estudiante, Profesor

# Create your views here.

def index(request):
    return render(request, 'index.html')
    
def listaAsignaturas(request):
	lista_asignaturas = Asignatura.objects.all()
	context = {'lista_asignaturas': lista_asignaturas}
	return render(request, 'indexAsignaturas.html', context)
    
def getAsignatura(request, nombre_id):
	return HttpResponse("Asignatura %s" % nombre_id)
	
def listaEstudiantes(request):
	lista_estudiantes = Estudiante.objects.all()
	context = {'lista_estudiantes': lista_estudiantes}
	return render(request, 'indexEstudiantes.html', context)
    
def getEstudiante(request, dni):
	return HttpResponse("Estudiante con DNI = %s" % dni)

def listaProfesores(request):
	lista_profesores = Profesor.objects.all()
	context = {'lista_profesores': lista_profesores}
	return render(request, 'indexProfesores.html', context)
    
def getProfesor(request, dni):
	return HttpResponse("Profesor con DNI = %s" % dni)
