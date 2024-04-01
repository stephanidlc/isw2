from django.test import SimpleTestCase
from django.urls import reverse, resolve
from app.views.estudiante.views import *

class TestUrls(SimpleTestCase):
  #Gestionar Solicitudes
  def test_list_url_resolves(self):
    url = reverse('listar_solicitudes')
    self.assertEquals(resolve(url).func.view_class, ListarSolicitudes)

  def test_detail_url_resolves(self):
    url = reverse('visualizar_solicitud', args='1')
    self.assertEquals(resolve(url).func.view_class, VisualizarSolicitud)
    
  def test_create_url_resolves(self):
    url = reverse('crear_solicitud')
    self.assertEquals(resolve(url).func.view_class, CrearSolicitud)
  
  def test_update_url_resolves(self):
    url = reverse('modificar_solicitud', args='1')
    self.assertEquals(resolve(url).func.view_class, ModificarSolicitud)
    
  def test_delete_url_resolves(self):
    url = reverse('eliminar_solicitud', args='1')
    self.assertEquals(resolve(url).func.view_class, EliminarSolicitud)
    
