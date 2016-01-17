from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from .models import Asignatura, Usuario
from .forms import DatosUsuario, DatosAsignatura
from django.contrib.auth.models import User
from operator import attrgetter
import settings
import os

# Create your views here.

def index(request):
    return render(request, 'index.html')
    
def listaAsignaturas(request):
	lista_asignaturas = Asignatura.objects.all()
	lista_asignaturas = sorted(lista_asignaturas, key=attrgetter('nombre'))
	if request.user.is_active:
		if Usuario.objects.filter(nick = request.user):
			usuario = Usuario.objects.get(nick = request.user)
			context = {'lista_asignaturas': lista_asignaturas, 'usuario': usuario}
		else:
			context = {'lista_asignaturas': lista_asignaturas}
	else:
		context = {'lista_asignaturas': lista_asignaturas}
	return render(request, 'indexAsignaturas.html', context)
    
def getAsignatura(request, n_id):
	asignatura = Asignatura.objects.get(nombre_id = n_id)
	profesor = Usuario.objects.get(nombre = asignatura.creador)
	if request.user.is_active:
		alumnos = Usuario.objects.filter(tipo='ESTUDIANTE')
		lista_alumnos = []
		for alumno in alumnos:
			if alumno.asignaturas.filter(nombre_id = n_id):
				lista_alumnos.append(alumno)
		if Usuario.objects.filter(nick = request.user):
			usuario = Usuario.objects.get(nick = request.user)
			if usuario.asignaturas.filter(nombre = asignatura.nombre):
				dentro=True
			else:
				dentro=False
			context = {'nombre_id': n_id, 'asignatura': asignatura, 'usuario': usuario, 'profesor': profesor, 'dentro': dentro, 'lista_alumnos': lista_alumnos}
		else:
			context = {'nombre_id': n_id, 'asignatura': asignatura, 'profesor': profesor, 'lista_alumnos': lista_alumnos}
	else:
		context = {'nombre_id': n_id, 'asignatura': asignatura, 'profesor': profesor}
	return render(request, 'datosAsignatura.html', context)
	
def listaEstudiantes(request):
	lista_estudiantes = Usuario.objects.filter(tipo='ESTUDIANTE')
	lista_estudiantes = sorted(lista_estudiantes, key=attrgetter('nombre'))
	context = {'lista_estudiantes': lista_estudiantes}
	return render(request, 'indexEstudiantes.html', context)

def listaProfesores(request):
	lista_profesores = Usuario.objects.filter(tipo='PROFESOR')
	lista_profesores = sorted(lista_profesores, key=attrgetter('nombre'))
	context = {'lista_profesores': lista_profesores}
	return render(request, 'indexProfesores.html', context)
	    
def getUsuario(request, nickuser):
	if Usuario.objects.filter(nick = request.user):
		usuario = Usuario.objects.get(nick = User.objects.get(username = nickuser))
		return render_to_response('perfilUsuario.html', {'nick': nickuser, 'usuario': usuario}, context_instance=RequestContext(request))
	else:
		return render(request, 'avisoCuenta.html')

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
		form = DatosUsuario(request.POST, request.FILES) 
		if form.is_valid():  # All validation rules pass
			if Usuario.objects.filter(nick = request.user):  # If User exists, modify his data
				Usuario.objects.filter(nick = request.user).update(nombre = form.cleaned_data["nombre"], email = form.cleaned_data["email"], tipo = form.cleaned_data["tipo"])
				usuario = Usuario.objects.get(nick = request.user)
				if 'imagen' in request.FILES:
					usuario.imagen = request.FILES['imagen']
				else:
					usuario.imagen = "perfiles/anonimo.png"
				usuario.save()
			else:
				# Process the data in form.cleaned_data
				usuario = Usuario.objects.create(nick = request.user, nombre = form.cleaned_data["nombre"], email = form.cleaned_data["email"], tipo = form.cleaned_data["tipo"])
				if 'imagen' in request.FILES:
					usuario.imagen = request.FILES['imagen']
				else:
					usuario.imagen = "perfiles/anonimo.png"
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
				web = form.cleaned_data["web"],
				creador = usuario.nombre
			)
			asignatura.save()  # Save new user attributes
			usuario.asignaturas.add(asignatura)
			usuario.save()
			
			return HttpResponseRedirect('asignaturacreada')  # Redirect after POST
	else: 
		form = DatosAsignatura()  
	return render_to_response('nuevaAsignatura.html', {'form': form}, context_instance=RequestContext(request)) 
	
def asignaturaCreada(request):
	return render(request, 'asignaturaCreada.html')
	
def borrarAsignatura(request, n_id):
	asignatura = Asignatura.objects.get(nombre_id = n_id)
	for usuario in Usuario.objects.all():
		usuario.asignaturas.remove(asignatura)
	Asignatura.objects.get(nombre = asignatura.nombre).delete()
	return misAsignaturas(request)
	
def unirAsignatura(request, n_id):
	asignatura = Asignatura.objects.get(nombre_id = n_id)
	usuario = Usuario.objects.get(nick = request.user)
	if not usuario.asignaturas.filter(nombre_id = n_id):
		usuario.asignaturas.add(asignatura)
		usuario.save()
	return misAsignaturas(request)
	
def salirAsignatura(request, n_id):
	asignatura = Asignatura.objects.get(nombre_id = n_id)
	usuario = Usuario.objects.get(nick = request.user)
	if usuario.asignaturas.filter(nombre_id = n_id):
		usuario.asignaturas.remove(asignatura)
		usuario.save()
	return misAsignaturas(request)	

def misAsignaturas(request):
	if Usuario.objects.filter(nick = request.user):
		usuario = Usuario.objects.get(nick = request.user)
		lista_asignaturas = usuario.asignaturas.all()
		context = {'lista_asignaturas': lista_asignaturas}
		return render(request, 'asignaturasUsuario.html', context)
	return render(request, 'avisoCuenta.html')
	
def miPerfil(request):
	return getUsuario(request, request.user.username)
