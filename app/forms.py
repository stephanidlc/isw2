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
      'tipo' : forms.Select(attrs={'class':'form-select'}),
      'motivo' : forms.Textarea(attrs={'class':'form-control', 'rows':'50'})
    }
    

class ModificarEstadoSolicitudForm(forms.ModelForm):
  class Meta:
    model = Solicitud
    fields = ['estado']
    widgets = {
      'estado': forms.Select(attrs={'class':'form-select'})
    }


class EstudianteForm(forms.Form):
  nombre = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
  apellidos = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
  nombre_usuario = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
  password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
  grupo = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
  anno = forms.IntegerField(widget=forms.TextInput(attrs={'class':'form-control'}))