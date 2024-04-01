from django.forms import BaseModelForm
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, UpdateView
from app.models import Reporte, Solicitud, NotificacionSolicitudEstudiante, NotificacionSolicitudSecretario
from app.forms import ModificarEstadoSolicitudForm
from django.urls import reverse_lazy

class ListarReportes(ListView):
  rol = 'decano'
  model = Reporte 
  template_name = 'decano/reportes/listar_reportes.html'
  
  
class VisuzalizarReporte(DetailView):
  rol = 'decano'
  model = Reporte
  template_name = 'decano/reportes/visualizar_reporte.html'
  context_object_name = 'reporte'
  
  
class ListarSolicitudes(ListView):
  rol = 'decano'
  model = Solicitud
  template_name = 'decano/solicitudes/listar_solicitudes.html'


class VisuzalizarSolicitud(DetailView):
  rol = 'decano'
  model = Solicitud
  template_name = 'decano/solicitudes/visualizar_solicitud.html'
  context_object_name = 'solicitud'
  

class ModificarEstadoSolicitud(UpdateView):
  rol = 'decano'
  model = Solicitud
  form_class = ModificarEstadoSolicitudForm
  context_object_name = 'solicitud'
  template_name = 'decano/solicitudes/modificar_estado_solicitud.html'
  
  def get_success_url(self):
    return reverse_lazy('visualizar_solicitud_decano', kwargs={'pk':self.object.pk})
  
  def form_valid(self, form):
    sol = self.get_object()
    NotificacionSolicitudSecretario.objects.create(
      estudiante = sol.estudiante,
      tipo = sol.tipo,
      motivo = sol.motivo,
      estado = form.cleaned_data['estado'],
      fecha = sol.fecha
    )
    NotificacionSolicitudEstudiante.objects.create(
      estudiante = sol.estudiante,
      tipo = sol.tipo,
      motivo = sol.motivo,
      estado = form.cleaned_data['estado'],
      fecha = sol.fecha
    )
    return super().form_valid(form)