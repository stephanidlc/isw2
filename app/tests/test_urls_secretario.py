from django.test import SimpleTestCase
from django.urls import reverse, resolve
from app.views.secretario.views import *

class TestUrls(SimpleTestCase):
  #Gestionar Estudiante
  def test_list_url_resolves(self):
    url = reverse('listar_estudiantes')
    self.assertEquals(resolve(url).func.view_class, ListarEstudiantes)

  def test_detail_url_resolves(self):
    url = reverse('visualizar_estudiante', args='1')
    self.assertEquals(resolve(url).func.view_class, VisualizarEstudiante)
    
  def test_create_url_resolves(self):
    url = reverse('crear_estudiante')
    self.assertEquals(resolve(url).func, crear_estudiante)
  
  def test_update_url_resolves(self):
    url = reverse('modificar_estudiante', args='1')
    self.assertEquals(resolve(url).func, modificar_estudiante)
    
  def test_delete_url_resolves(self):
    url = reverse('eliminar_estudiante', args='1')
    self.assertEquals(resolve(url).func.view_class, EliminarEstudiante)
  