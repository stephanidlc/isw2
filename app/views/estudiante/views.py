from django.views.generic import CreateView, UpdateView, DeleteView, DetailView, ListView
from django.urls import reverse_lazy
from app.models import Solicitud, NotificacionSolicitudEstudiante
from app.forms import SolicitudForm

class ListarSolicitudes(ListView):
  rol = 'estudiante'
  model = Solicitud
  template_name = 'estudiante/solicitudes/listar_solicitudes.html'
  
  def get_queryset(self):
      return Solicitud.objects.filter(estudiante = self.request.user.usuario.estudiante).order_by('-fecha')
  
    
class VisualizarSolicitud(DetailView):
  rol = 'estudiante'
  model = Solicitud
  template_name = 'estudiante/solicitudes/visualizar_solicitud.html'
  context_object_name = 'solicitud'

class CrearSolicitud(CreateView):
  rol = 'estudiante'
  model = Solicitud
  form_class = SolicitudForm
  template_name = 'estudiante/solicitudes/crear_solicitud.html'
  success_url = reverse_lazy('listar_solicitudes')
  
  def form_valid(self, form):
     form.instance.estudiante = self.request.user.usuario.estudiante
     return super().form_valid(form)

class ModificarSolicitud(UpdateView):
  rol = 'estudiante'
  model = Solicitud
  form_class = SolicitudForm
  template_name = 'estudiante/solicitudes/crear_solicitud.html'
  success_url = reverse_lazy('listar_solicitudes')
  
  
class EliminarSolicitud(DeleteView):
  rol = 'estudiante'
  model = Solicitud
  template_name = 'layout/eliminar.html'
  success_url = reverse_lazy('listar_solicitudes')
  
  def get_context_data(self, **kwargs):
    ctx = super().get_context_data(**kwargs)
    ctx['mensaje'] = '¿Seguro que desea eliminar esta solicitud?'
    return ctx
  

class ListarNotificaciones(ListView):
  rol = 'estudiante'
  model = NotificacionSolicitudEstudiante
  template_name = 'estudiante/notificaciones/listar_notificaciones.html'
  
  def get_queryset(self):
    return NotificacionSolicitudEstudiante.objects.filter(estudiante = self.request.user.usuario.estudiante).order_by('-fecha_notificacion')
  

class VisualizarNotificacion(DetailView):
  rol = 'estudiante'
  model = NotificacionSolicitudEstudiante
  context_object_name = 'notificacion'
  template_name = 'estudiante/notificaciones/visualizar_notificacion.html'
  
  def dispatch(self, request, *args, **kwargs):
    a = self.get_object()
    a.visto = True
    a.save()
    return super().dispatch(request, *args, **kwargs)
  

class EliminarNotificacion(DeleteView):
  rol = 'estudiante'
  model = NotificacionSolicitudEstudiante
  template_name = 'layout/eliminar.html'
  success_url = reverse_lazy('listar_notificaciones_estudiante')
  
  def get_context_data(self, **kwargs):
    ctx = super().get_context_data(**kwargs)
    ctx['mensaje'] = '¿Seguro que desea eliminar la notificación?'
    return ctx