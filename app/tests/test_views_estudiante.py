from django.test import TestCase, Client
from django.contrib.auth import authenticate, login
from django.urls import reverse
from app.models import *
from django.test import RequestFactory

class TestViews(TestCase):
  
  def setUp(self):
    self.estudiante = Estudiante.objects.create(
      usuario = User.objects.create(
        username = 'usuarioprueba',
        password = 'kjkszpj01' 
      ), 
      grupo = '3201',
      anno=4
      )
    self.client.force_login(self.estudiante.usuario)
    self.solicitud = Solicitud.objects.create(
      tipo = "Baja",
      motivo = 'Texto de Prueba',
      estudiante = self.estudiante
    )
    
  def test_solicitudes_list_GET(self):
    response = self.client.get(reverse('listar_solicitudes'))
    self.assertEqual(response.status_code, 200)
    self.assertTemplateUsed(response, 'estudiante/solicitudes/listar_solicitudes.html')
    
  def test_solicitud_create_get(self):
    response = self.client.get(reverse('crear_solicitud'))
    self.assertEqual(response.status_code, 200)
    self.assertTemplateUsed(response, 'estudiante/solicitudes/crear_solicitud.html')
  
  def test_solicitud_update_get(self):
    response = self.client.get(reverse('modificar_solicitud', kwargs={'pk':self.solicitud.pk}))
    self.assertEqual(response.status_code, 200)
    self.assertTemplateUsed(response, 'estudiante/solicitudes/crear_solicitud.html')
    
  def test_solicitud_detail_GET(self):
    response = self.client.get(reverse('visualizar_solicitud', kwargs={'pk':self.solicitud.pk}))
    self.assertEqual(response.status_code, 200)
    self.assertTemplateUsed(response, 'estudiante/solicitudes/visualizar_solicitud.html')
    
  def test_solicitud_delete_GET(self):
    response = self.client.get(reverse('eliminar_solicitud', kwargs={'pk':self.solicitud.pk}))
    self.assertEqual(response.status_code, 200)
    self.assertTemplateUsed(response, 'layout/eliminar.html')