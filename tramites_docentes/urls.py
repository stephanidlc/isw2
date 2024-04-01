from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.views.autenticar.urls')),
    path('estudiante/', include('app.views.estudiante.urls')),
    path('secretario/', include('app.views.secretario.urls')),
    path('decano/', include('app.views.decano.urls')),
]
