from django import forms
from django.forms import ModelForm
from .models import Usuario, Asignatura


class DatosUsuario(ModelForm):
    class Meta:
        model = Usuario
        fields = ['nombre', 'email', 'tipo', 'imagen']
        widgets = {
			'tipo': forms.RadioSelect()
		}
		
class DatosAsignatura(ModelForm):
	class Meta:
		model = Asignatura
		fields = ['nombre', 'nombre_id', 'centro', 'titulacion', 'curso', 'web']
