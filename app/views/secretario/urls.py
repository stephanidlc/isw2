from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
  path('estudiantes/', ListarEstudiantes.as_view(), name='listar_estudiantes'),
  path('estudiantes/<int:pk>/', VisualizarEstudiante.as_view(), name='visualizar_estudiante'),
  path('estudiantes/crear_estudiante/', CrearEstudiante.as_view(), name='crear_estudiante'),
  path('estudiantes/modificar_estudiante/<int:pk>/', ModificarEstudiante.as_view(), name='modificar_estudiante'),
  path('estudiantes/eliminar_estudiante/<int:pk>/', EliminarEstudiante.as_view(), name='eliminar_estudiante'),
  path('reportes/', ListarReportes.as_view(), name='listar_reportes'),
  path('reportes/<int:pk>/', VisuzalizarReporte.as_view(), name='visualizar_reporte'),
  path('reportes/crear_reporte/', CrearReporte.as_view(), name='crear_reporte'),
  path('reportes/eliminar_reporte/<int:pk>/', EliminarReporte.as_view(), name='eliminar_reporte'),
  path('solicitudes/', ListarSolicitudes.as_view(), name='listar_solicitudes_secretario'),
  path('solicitudes/<int:pk>/', VisualizarSolicitud.as_view(), name='visualizar_solicitud_secretario'), 
  path('notificaciones/', ListarNotificaciones.as_view(), name='listar_notificaciones_secretario'),
  path('notificaciones/<int:pk>/', VisualizarNotificacion.as_view(), name='visualizar_notificacion_secretario'),
  path('notificaciones/eliminar_notificacion/<int:pk>/', EliminarNotificacion.as_view(), name='eliminar_notificacion_secretario'),
]
