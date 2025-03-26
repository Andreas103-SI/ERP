# finanzas/models.py
from django.db import models
from ventas.models import Venta
from pedidos.models import Pedido
from empleados.models import Empleado

# Finanzas
class Finanzas(models.Model):
    TIPO_CHOICES = [
        ('Ingreso', 'Ingreso'),
        ('Egreso', 'Egreso'),
    ]

    id_finanzas = models.AutoField(primary_key=True)
    tipo = models.CharField(max_length=10, choices=TIPO_CHOICES)
    venta = models.ForeignKey(Venta, on_delete=models.CASCADE, null=True, blank=True)
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, null=True, blank=True)
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE, null=True, blank=True)
    descripcion = models.CharField(max_length=100)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    iva = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    fecha = models.DateField()

    def __str__(self):
        return f"{self.tipo} - {self.descripcion} - {self.fecha}"

class Gasto(models.Model):
    CATEGORIAS = [
        ('nomina', 'Nómina'),
        ('servicios', 'Servicios'),
        ('materiales', 'Materiales'),
        ('otros', 'Otros'),
    ]

    descripcion = models.CharField(max_length=200)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.CharField(max_length=20, choices=CATEGORIAS)
    fecha = models.DateField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.descripcion} - {self.monto}"

    class Meta:
        verbose_name = 'Gasto'
        verbose_name_plural = 'Gastos'

# Create your models here.
