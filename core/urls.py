from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('descartadores/', include('descartadores.urls')),
    path('descartes/', include('descartes.urls')),
    path('ecopontos/', include('ecopontos.urls')),
    path('usuarios/', include('usuarios.urls')),
]
