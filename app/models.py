from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Usuario(models.Model):
  usuario = models.OneToOneField(User, on_delete = models.CASCADE, primary_key = 1)
  rol = models.CharField(max_length = 20, blank = 0, null = 0)

  class Meta:
    verbose_name = 'Usuario'
    verbose_name_plural = 'Usuarios'
    db_table = 'usuario'


class Estudiante(Usuario):
  grupo = models.CharField(max_length = 20, null = 0, blank = 0)
  anno = models.IntegerField(default = 1)
  
  class Meta:
    verbose_name = 'Estudiante'
    verbose_name_plural = 'Estudiantes'
    db_table = 'estudiantes'
  
  
class Solicitud(models.Model):
  tipo_opciones = [
    ('Baja', 'Baja'),
    ('Continuidad de Estudios', 'Continuidad de Estudios'),
    ('Licencia', 'Licencia'),
    ('Traslado', 'Traslado'),
    ]
  estado_opciones = [
    ('Aprobado','Aprobado'),
    ('Denegado','Denegado'),
  ]
  tipo = models.CharField(max_length = 255, null = 0, blank = 0, choices = tipo_opciones, default = 'Baja')
  motivo = models.TextField(blank = 0, null = 0)
  fecha = models.DateField(default = timezone.now)
  estado = models.CharField(max_length = 50, choices = estado_opciones, default = 'Pendiente')
  estudiante = models.ForeignKey(Estudiante, on_delete = models.CASCADE)
  
  class Meta:
    verbose_name = 'Solicitud'
    verbose_name_plural = 'Solicitudes'
    db_table = 'solicitudes'
  

class Reporte(models.Model):
  bajas = models.IntegerField()
  continuidad = models.IntegerField()
  licencias = models.IntegerField()
  traslados = models.IntegerField()
  bajas_aprobadas = models.IntegerField()
  continuidad_aprobados = models.IntegerField()
  licencias_aprobadas = models.IntegerField()
  traslados_aprobados = models.IntegerField()
  fecha = models.DateTimeField(default = timezone.now)
  
  class Meta:
    verbose_name = 'Reporte'
    verbose_name_plural = 'Reportes'
    db_table = 'reportes'
  

class NotificacionSolicitud(models.Model):
  estudiante = models.ForeignKey(Estudiante, on_delete = models.CASCADE) 
  tipo = models.CharField(max_length = 255, null = 0, blank = 0)
  motivo = models.TextField(blank = 0, null = 0)
  estado = models.CharField(max_length = 50, blank = 0, null = 0)
  fecha = models.DateField()
  fecha_notificacion = models.DateField(default = timezone.now)
  visto = models.BooleanField(default=0)
  
  class Meta:
    verbose_name = 'Notificacion'
    verbose_name_plural = 'Notifiaciones'
    db_table = 'notificaciones'
  
class NotificacionSolicitudEstudiante(NotificacionSolicitud):
  class Meta:
    verbose_name = 'NotificacionEstudiante'
    verbose_name_plural = 'NotifiacionesEstudiante'
    db_table = 'notificaciones_estudiante'

class NotificacionSolicitudSecretario(NotificacionSolicitud):
  class Meta:
    verbose_name = 'NotificacionSecretario'
    verbose_name_plural = 'NotifiacionesSecretario'
    db_table = 'notificaciones_secretario'

  
