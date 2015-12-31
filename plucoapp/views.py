from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from .models import Asignatura, Usuario
from .forms import DatosUsuario, DatosAsignatura
from django.contrib.auth.models import User

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
	lista_estudiantes = Usuario.objects.filter(tipo='ESTUDIANTE')
	context = {'lista_estudiantes': lista_estudiantes}
	return render(request, 'indexEstudiantes.html', context)

def listaProfesores(request):
	lista_profesores = Usuario.objects.filter(tipo='PROFESOR')
	context = {'lista_profesores': lista_profesores}
	return render(request, 'indexProfesores.html', context)
	    
def getUsuario(request, nickuser):
	usuario = Usuario.objects.get(nick = User.objects.get(username = nickuser))
	return render_to_response('perfilUsuario.html', {'nick': nickuser, 'usuario': usuario}, context_instance=RequestContext(request))

def registrarUsuario(request): 
	if request.method == 'POST':  # If the form has been submitted...
		form = UserCreationForm(request.POST) 
		if form.is_valid():  # All validation rules pass
			# Process the data in form.cleaned_data
			form.save()  # Save new user attributes
			
			return HttpResponseRedirect('registrocorrecto')  # Redirect after POST
	else: 
		form = UserCreationForm() 
	return render_to_response('registroUsuario.html', {'form': form}, context_instance=RequestContext(request)) 
	
def editarUsuario(request): 
	if request.method == 'POST':  # If the form has been submitted...
		form = DatosUsuario(request.POST) 
		if form.is_valid():  # All validation rules pass
			if Usuario.objects.filter(nick = request.user):  # If User exists, modify his data
				Usuario.objects.filter(nick = request.user).update(nombre = form.cleaned_data["nombre"], email = form.cleaned_data["email"], tipo = form.cleaned_data["tipo"])
			else:
				# Process the data in form.cleaned_data
				usuario = Usuario.objects.create(nick = request.user, nombre = form.cleaned_data["nombre"], email = form.cleaned_data["email"], tipo = form.cleaned_data["tipo"])
				usuario.save()  # Save new user attributes
			
			return HttpResponseRedirect('/')  # Redirect after POST
	else:
		form = DatosUsuario()
	return render_to_response('editarUsuario.html', {'form': form}, context_instance=RequestContext(request)) 

def usuarioRegistrado(request):
	return render(request, 'usuarioRegistrado.html')
	
def crearAsignatura(request):
	if request.method == 'POST':  # If the form has been submitted...
		form = DatosAsignatura(request.POST) 
		if form.is_valid():  # All validation rules pass
			# Process the data in form.cleaned_data
			usuario = Usuario.objects.get(nick = request.user)
			asignatura = Asignatura.objects.create(
				nombre = form.cleaned_data["nombre"],
				nombre_id = form.cleaned_data["nombre_id"],
				centro = form.cleaned_data["centro"],
				titulacion = form.cleaned_data["titulacion"],
				curso = form.cleaned_data["curso"],
				creador = usuario.nombre
			)
			asignatura.save()  # Save new user attributes
			
			return HttpResponseRedirect('asignaturacreada')  # Redirect after POST
	else: 
		form = DatosAsignatura()  
	return render_to_response('nuevaAsignatura.html', {'form': form}, context_instance=RequestContext(request)) 
	
def asignaturaCreada(request):
	return render(request, 'asignaturaCreada.html')
