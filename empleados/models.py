from django.db import models
from django.core.exceptions import ValidationError

class Empleado(models.Model):
    id_empleado = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    dni = models.CharField(max_length=20, unique=True)
    telefono = models.CharField(max_length=15)
    direccion = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(unique=True, blank=False)  # No permite cadenas vacías
    puesto = models.CharField(max_length=50, blank=False)  # No permite cadenas vacías
    salario = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_contratacion = models.DateField(blank=True, null=True)  # Nuevo campo

    def __str__(self):
        return f"{self.nombre} {self.apellido} - {self.puesto}"

    def save(self, *args, **kwargs):
        # Ejecuta la validación completa antes de guardar
        self.full_clean()
        super().save(*args, **kwargs)