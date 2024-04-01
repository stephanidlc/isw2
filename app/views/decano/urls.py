from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
  path('reportes/', ListarReportes.as_view(), name='listar_reportes_decano'),
  path('reportes/visualizar_reporte/<int:pk>/', VisuzalizarReporte.as_view(), name='visualizar_reporte_decano'),
  path('solicitudes/', ListarSolicitudes.as_view(), name='listar_solicitudes_decano'),
  path('solicitudes/<int:pk>/', VisuzalizarSolicitud.as_view(), name='visualizar_solicitud_decano'), 
  path('solicitudes/modificar_estado_solicitud/<int:pk>/', ModificarEstadoSolicitud.as_view(), name='modificar_estado_solicitud'), 
]
