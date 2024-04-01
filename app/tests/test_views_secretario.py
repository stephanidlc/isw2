from django.test import TestCase, Client
from django.contrib.auth import authenticate, login
from django.urls import reverse
from app.models import *
from django.test import RequestFactory

class TestViews(TestCase):
  
  def setUp(self):
    self.secretario = Usuario.objects.create(
      usuario = User.objects.create(
        username = 'secretario',
        password = 'kjkszpj01' 
      ),
      rol = 'secretario'
    )
    self.estudiante = Estudiante.objects.create(
      usuario = User.objects.create(
        username = 'usuarioprueba',
        password = 'kjkszpj01' 
      ), 
      grupo = '3201',
      anno=4
      )
    self.client.force_login(self.secretario.usuario)
    
  def test_estudiantes_list_GET(self):
    response = self.client.get(reverse('listar_estudiantes'))
    self.assertEqual(response.status_code, 200)
    self.assertTemplateUsed(response, 'secretario/estudiantes/listar_estudiantes.html')
    
  def test_estudiante_create_get(self):
    response = self.client.get(reverse('crear_estudiante'))
    self.assertEqual(response.status_code, 200)
    self.assertTemplateUsed(response, 'secretario/estudiantes/crear_estudiante.html')
  
  def test_estudiante_update_get(self):
    response = self.client.get(reverse('modificar_estudiante', kwargs={'pk':self.estudiante.pk}))
    self.assertEqual(response.status_code, 200)
    self.assertTemplateUsed(response, 'secretario/estudiantes/crear_estudiante.html')
    
  def test_estudiante_detail_GET(self):
    response = self.client.get(reverse('visualizar_estudiante', kwargs={'pk':self.estudiante.pk}))
    self.assertEqual(response.status_code, 200)
    self.assertTemplateUsed(response, 'secretario/estudiantes/visualizar_estudiante.html')
    
  def test_estudiante_delete_GET(self):
    response = self.client.get(reverse('eliminar_estudiante', kwargs={'pk':self.estudiante.pk}))
    self.assertEqual(response.status_code, 200)
    self.assertTemplateUsed(response, 'layout/eliminar.html')