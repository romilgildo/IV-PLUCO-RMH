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
import settings

urlpatterns = patterns ('',
    url(r'^$', views.index, name='index'),
    url(r'^asignaturas/$', views.listaAsignaturas, name='lista_asignaturas'),
    url(r'^asignaturas/(?P<n_id>[a-zA-Z0-9-]+)/$', views.getAsignatura, name='asignatura'),
	url(r'^estudiantes/$', views.listaEstudiantes, name='lista_estudiantes'),
    url(r'^estudiantes/(?P<nickuser>[a-zA-Z]+)/$', views.getUsuario, name='estudiante'),
    url(r'^profesores/$', views.listaProfesores, name='lista_profesores'),
    url(r'^profesores/(?P<nickuser>[a-zA-Z]+)/$', views.getUsuario, name='profesor'),
    url(r'^registrousuario$', views.registrarUsuario, name='registro_usuario'),
    url(r'^registrocorrecto$', views.usuarioRegistrado, name='registro_correcto'),
	url(r'^editarusuario$', views.editarUsuario, name='editar_usuario'),
    url(r'^nuevaasignatura$', views.crearAsignatura, name='nueva_asignatura'),
    url(r'^asignaturacreada$', views.asignaturaCreada, name='asignatura_creada'),
    url(r'^borrarasignatura/(?P<n_id>[a-zA-Z0-9-]+)', views.borrarAsignatura, name='borrar_asignatura'),
    url(r'^unirse/(?P<n_id>[a-zA-Z0-9-]+)', views.unirAsignatura, name='unir_asignatura'),
    url(r'^salirse/(?P<n_id>[a-zA-Z0-9-]+)', views.salirAsignatura, name='salir_asignatura'),
    url(r'^misasignaturas$', views.misAsignaturas, name='mis_asignaturas'),
    url(r'^miperfil$', views.miPerfil, name='mi_perfil'),
    url(r'^login$', login, {'template_name': 'index.html', }, name="login"),
    url(r'^logout$', logout, {'template_name': 'index.html', }, name="logout"),
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += staticfiles_urlpatterns()

if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT}))
