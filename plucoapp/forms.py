from django import forms
from django.forms import ModelForm
from .models import Usuario


class DatosUsuario(ModelForm):
    class Meta:
        model = Usuario
        fields = ['nombre', 'email', 'tipo']
        widgets = {
			'tipo': forms.RadioSelect()
		}
