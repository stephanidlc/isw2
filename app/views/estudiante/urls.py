from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
  path('solicitudes/', ListarSolicitudes.as_view(), name='listar_solicitudes'),
  path('solicitudes/<int:pk>/', VisualizarSolicitud.as_view(), name='visualizar_solicitud'),
  path('solicitudes/crear_solicitud/', CrearSolicitud.as_view(), name='crear_solicitud'),
  path('solicitudes/modificar_solicitud/<int:pk>/', ModificarSolicitud.as_view(), name='modificar_solicitud'),
  path('solicitudes/eliminar_solicitud/<int:pk>/', EliminarSolicitud.as_view(), name='eliminar_solicitud'),
  path('notificaciones/', ListarNotificaciones.as_view(), name='listar_notificaciones_estudiante'),
  path('notificaciones/<int:pk>/', VisualizarNotificacion.as_view(), name='visualizar_notificacion_estudiante'),
  path('notificaciones/eliminar_notificacion/<int:pk>/', EliminarNotificacion.as_view(), name='eliminar_notificacion_estudiante'),
]
