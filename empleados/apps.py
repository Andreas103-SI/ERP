from django.apps import AppConfig


# empleados/apps.py
from django.apps import AppConfig

class EmpleadosConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'empleados'

    def ready(self):
        import empleados.signals  # Importa las señales