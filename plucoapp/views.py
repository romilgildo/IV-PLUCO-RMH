from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from plucoapp.models import Asignatura

# Create your views here.

def index(request):
    return render(request, 'index.html')
    
def listaAsignaturas(request):
	lista_ultimas_asignaturas = Asignatura.objects.all()[:5]
	context = {'lista_ultimas_asignaturas': lista_ultimas_asignaturas}
	return render(request, 'indexAsignaturas.html', context)
    
def getAsignatura(request, asig_nombre):
	return HttpResponse("Asignatura %s" % asig_nombre)
