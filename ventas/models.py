from django.db import models
from inventario.models import Vehiculo  # Importamos Vehiculo desde la app inventario

# Cliente
class Cliente(models.Model):
    id_cliente = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    dni_pasaporte = models.CharField(max_length=20, unique=True)
    telefono = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    direccion = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

# Venta
class Venta(models.Model):
    id_venta = models.AutoField(primary_key=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    presupuesto = models.DecimalField(max_digits=10, decimal_places=2)
    contrato = models.TextField()
    fecha = models.DateField()
    valor_venta = models.DecimalField(max_digits=10, decimal_places=2)
    iva = models.DecimalField(max_digits=10, decimal_places=2)
    total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Venta {self.id_venta} - Cliente: {self.cliente}"

# Venta_Vehículo (Tabla intermedia)
class VentaVehiculo(models.Model):
    venta = models.ForeignKey(Venta, on_delete=models.CASCADE)
    vehiculo = models.ForeignKey(Vehiculo, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('venta', 'vehiculo')

    def __str__(self):
        return f"Venta {self.venta.id_venta} - Vehículo {self.vehiculo}"