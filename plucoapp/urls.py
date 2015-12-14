"""pluco URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url, patterns
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
from django.contrib.auth.views import login, logout
from plucoapp import views

urlpatterns = patterns ('',
    url(r'^$', views.index, name='index'),
    url(r'^asignaturas/$', views.listaAsignaturas, name='lista_asignaturas'),
    url(r'^asignaturas/(?P<nombre_id>[a-zA-Z0-9-]+)/$', views.getAsignatura, name='asignatura'),
	url(r'^estudiantes/$', views.listaEstudiantes, name='lista_estudiantes'),
    url(r'^estudiantes/(?P<dni>[a-zA-Z0-9-]+)/$', views.getEstudiante, name='estudiante'),
    url(r'^profesores/$', views.listaProfesores, name='lista_profesores'),
    url(r'^profesores/(?P<dni>[a-zA-Z0-9-]+)/$', views.getProfesor, name='profesor'),
    url(r'^nuevousuario$', views.registroUsuario, name='registro_usuario'),
    url(r'^registrousuario$', views.completarRegistro, name='registro_usuarioC'),
    url(r'^registrocorrecto$', views.usuarioRegistrado, name='registro_correcto'),
    url(r'^login$', login, {'template_name': 'index.html', }, name="login"),
    url(r'^logout$', logout, {'template_name': 'index.html', }, name="logout"),
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += staticfiles_urlpatterns()
