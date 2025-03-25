# erp_config/urls.py
from django.contrib import admin
from django.urls import path, include
from core.views import custom_logout
from django.contrib.auth.views import LoginView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('ventas/', include('ventas.urls')),
    path('inventario/', include('inventario.urls')),
    path('empleados/', include('empleados.urls')),
    path('pedidos/', include('pedidos.urls')),
    path('finanzas/', include('finanzas.urls')),
    path('reportes/', include('reportes.urls')),
    path('proveedores/', include('proveedores.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/logout/', custom_logout, name='logout'),  # Mantener compatibilidad con accounts/logout/
    path('home/', include('core.urls')),
    path('login/', LoginView.as_view(), name='login'),  # Mantener /login/ por compatibilidad
    path('logout/', custom_logout, name='logout'),  # Vista personalizada para logout
    path('password_change/', include('django.contrib.auth.urls')),  # Mantener las rutas de cambio de contraseña
    path('password_reset/', include('django.contrib.auth.urls')),  # Mantener las rutas de restablecimiento de contraseña
    path('', LoginView.as_view(template_name='registration/login.html'), name='login'),  # Raíz (/) muestra el login
]

