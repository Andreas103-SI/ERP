"""
URL configuration for erp_config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('ventas/', include('ventas.urls')),  # Vistas basadas en plantillas y APIs
    path('inventario/', include('inventario.urls')),
    path('empleados/', include('empleados.urls')),
    path('pedidos/', include('pedidos.urls')),
    path('finanzas/', include('finanzas.urls')),
    path('reportes/', include('reportes.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', include('core.urls')),  # Página principal
]