from django import forms 
from django.contrib.auth.forms import AuthenticationForm, UsernameField 
from .models import *

class LoginForm(AuthenticationForm):
  username = UsernameField(widget=forms.TextInput(attrs={'class':'form-control'}))
  password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))


class SolicitudForm(forms.ModelForm):
  class Meta:
    model = Solicitud
    fields = ['tipo', 'motivo']
    widgets = {
      'tipo' : forms.Select(),
      'motivo' : forms.Textarea()
    }
    

class ModificarEstadoSolicitudForm(forms.ModelForm):
  class Meta:
    model = Solicitud
    fields = ['estado']
    widgets = {
      'estado': forms.Select()
    }


class EstudianteForm(forms.Form):
  nombre = forms.CharField()
  apellidos = forms.CharField()
  nombre_usuario = forms.CharField()
  password = forms.CharField(widget=forms.PasswordInput())
  grupo = forms.CharField()
  anno = forms.IntegerField()