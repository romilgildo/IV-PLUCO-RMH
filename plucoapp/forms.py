from django import forms
from django.forms import ModelForm


class registroUsuario(ModelForm):
    class Meta:
        model = Usuario
        fields = ['nombre', 'email', 'tipo']
		widgets = {
			'tipo': forms.RadioSelect()
		}
