from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from django.contrib.auth.models import User
from .forms import NewUserForm
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
	
def registroUsuario(request): 
	if request.method == 'POST':  # If the form has been submitted...
		form = NewUserForm(request.POST) 
		if form.is_valid():  # All validation rules pass
			# Process the data in form.cleaned_data
			username = form.cleaned_data["username"]
			email = form.cleaned_data["email"]
			password = form.cleaned_data["password"]
			user = User.objects.create_user(username, email, password)
			user.save()  # Save new user attributes
			
			return HttpResponseRedirect('/')  # Redirect after POST
	else: 
		form = NewUserForm() 
	return render_to_response('registroUsuario.html', {'form': form}, context_instance=RequestContext(request)) 

