from django.http import HttpRequest
from django.views.generic import ListView, DetailView, DeleteView, View
from app.models import Estudiante, User, Reporte, Solicitud, NotificacionSolicitudSecretario
from app.forms import EstudianteForm
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

class ListarEstudiantes(ListView):
  rol = 'secretario'
  model = Estudiante
  template_name = 'secretario/estudiantes/listar_estudiantes.html'
  
  def get_queryset(self):
    return Estudiante.objects.all().order_by('usuario__first_name')


class VisualizarEstudiante(DetailView):
  rol = 'secretario'
  model = Estudiante
  template_name = 'secretario/estudiantes/visualizar_estudiante.html'
  context_object_name = 'estudiante'

class CrearEstudiante(View):
  rol = 'secretario'
  def post(self, request, *args, **kwargs):
    form = EstudianteForm(request.POST)
    if form.is_valid():
      try:
        usuario = User.objects.create(
        username = form.cleaned_data['nombre_usuario'], 
        password = form.cleaned_data['password'], 
        first_name = form.cleaned_data['nombre'], 
        last_name = form.cleaned_data['apellidos'])
        Estudiante.objects.create(
          usuario = usuario,
          rol = 'estudiante',
          grupo = form.cleaned_data['grupo'],
          anno = form.cleaned_data['anno']
        )
        return redirect('listar_estudiantes')
      except:
        ctx = {
          'operacion': 'crear',
          'form':form,
          'error':'Ya existe un usuario con el nombre de usuario insertado.',
          }
        return render(request, 'secretario/estudiantes/crear_estudiante.html', ctx)
  
  def get(self, request, *args, **kwargs):
    return render(request, 'secretario/estudiantes/crear_estudiante.html', {'operacion': 'crear','form':EstudianteForm()})
  

class ModificarEstudiante(View):
  rol = 'secretario'
  def post(self, request, *args, **kwargs):
    estudiante = Estudiante.objects.get(pk=kwargs.get('pk'))
    form = EstudianteForm(request.POST)
    if form.is_valid():
      try:
        estudiante.usuario.username = form.cleaned_data['nombre_usuario']
        estudiante.usuario.password = form.cleaned_data['password']
        estudiante.usuario.first_name = form.cleaned_data['nombre'] 
        estudiante.usuario.last_name = form.cleaned_data['apellidos']
        estudiante.grupo = form.cleaned_data['grupo']
        estudiante.anno = form.cleaned_data['anno']
        estudiante.usuario.save()
        estudiante.save()
        return redirect('listar_estudiantes')
      except:
        ctx = {
          'operacion': 'modificar',
          'form':form,
          'error':'Ya existe un usuario con el nombre de usuario insertado.',
          }
        return render(request, 'secretario/estudiantes/crear_estudiante.html', ctx)
  
  def get(self, request, *args, **kwargs):
    estudiante = Estudiante.objects.get(pk=kwargs.get('pk'))
    form = EstudianteForm(initial={
      'nombre_usuario': estudiante.usuario.username,
      'password': estudiante.usuario.password,
      'nombre' : estudiante.usuario.first_name,
      'apellidos' : estudiante.usuario.last_name,
      'grupo' : estudiante.grupo,
      'anno' : estudiante.anno
    }) 
    return render(request, 'secretario/estudiantes/crear_estudiante.html', {'operacion': 'crear', 'form':form})
  

class EliminarEstudiante(DeleteView):
  rol = 'secretario'
  model = User
  template_name = 'layout/eliminar.html'
  success_url = reverse_lazy('listar_estudiantes')
  
  def get_context_data(self, **kwargs):
    ctx = super().get_context_data(**kwargs)
    ctx['mensaje'] = '¿Seguro que desea eliminar este estudiante?'
    return ctx
  

class ListarReportes(ListView):
  rol = 'secretario'
  model = Reporte 
  template_name = 'secretario/reportes/listar_reportes.html'
  
  
class VisuzalizarReporte(DetailView):
  rol = 'secretario'
  model = Reporte
  template_name = 'secretario/reportes/visualizar_reporte.html'
  context_object_name = 'reporte'
  

class EliminarReporte(DeleteView):
  rol = 'secretario'
  model = Reporte
  template_name = 'layout/eliminar.html'
  success_url = reverse_lazy('listar_reportes')
  
  def get_context_data(self, **kwargs):
    ctx = super().get_context_data(**kwargs)
    ctx['mensaje'] = "¿Seguro que desea eliminar este reporte?"
    return ctx


class CrearReporte(View):
  rol = 'secretario'
  def setup(self, request: HttpRequest, *args, **kwargs):
    self.bajas = Solicitud.objects.filter(tipo = 'Baja').count()
    self.continuidad = Solicitud.objects.filter(tipo = 'Continuidad de Estudios').count()
    self.licencias = Solicitud.objects.filter(tipo = 'Licencia').count()
    self.traslados = Solicitud.objects.filter(tipo = 'Traslado').count()
    self.bajas_aprobadas = Solicitud.objects.filter(tipo = 'Baja', estado = 'aprobada').count()
    self.continuidad_aprobados = Solicitud.objects.filter(tipo = 'Continuidad de Estudios', estado = 'aprobada').count()
    self.licencias_aprobadas = Solicitud.objects.filter(tipo = 'Licencia', estado = 'aprobada').count()
    self.traslados_aprobados = Solicitud.objects.filter(tipo = 'Traslado', estado = 'aprobada').count()
    return super().setup(request, *args, **kwargs)
  
  def get(self, request, *args, **kwargs): 
    datos = {
      'bajas' : self.bajas,
      'continuidad' : self.continuidad,
      'licencias' : self.licencias,
      'traslados' : self.traslados,
      'bajas_aprobadas' : self.bajas_aprobadas,
      'continuidad_aprobados' : self.continuidad_aprobados,
      'licencias_aprobadas' : self.licencias_aprobadas,
      'traslados_aprobados' : self.traslados_aprobados,
    }
    return render(request, 'secretario/reportes/crear_reporte.html', datos)
  
  def post(self, request, *args, **kwargs):
    Reporte.objects.create(
      bajas = self.bajas,
      continuidad = self.continuidad,
      licencias = self.licencias,
      traslados = self.traslados,
      bajas_aprobadas = self.bajas_aprobadas,
      continuidad_aprobados = self.continuidad_aprobados,
      licencias_aprobadas = self.licencias_aprobadas,
      traslados_aprobados = self.traslados_aprobados
    )
    return redirect('listar_reportes')


class ListarSolicitudes(ListView):
  rol = 'secretario'
  model = Solicitud
  template_name = 'secretario/solicitudes/listar_solicitudes.html'


class VisualizarSolicitud(DetailView):
  rol = 'secretario'
  model = Solicitud
  template_name = 'secretario/solicitudes/visualizar_solicitud.html'
  
  
class ListarNotificaciones(ListView):
  rol = 'secretario'
  model = NotificacionSolicitudSecretario
  template_name = 'secretario/notificaciones/listar_notificaciones.html'

class VisualizarNotificacion(DetailView):
  rol = 'secretario'
  model = NotificacionSolicitudSecretario
  context_object_name = 'notificacion'
  template_name = 'secretario/notificaciones/visualizar_notificacion.html'
  
  def dispatch(self, request, *args, **kwargs):
    a = self.get_object()
    a.visto = True
    a.save()
    return super().dispatch(request, *args, **kwargs)
  
  
class EliminarNotificacion(DeleteView):
  rol = 'secretario'
  model = NotificacionSolicitudSecretario
  template_name = 'layout/eliminar.html'
  success_url = reverse_lazy('listar_notificaciones_secretario')
  
  def get_context_data(self, **kwargs):
    ctx = super().get_context_data(**kwargs)
    ctx['mensaje'] = '¿Seguro que desea eliminar la notificación?'
    return ctx