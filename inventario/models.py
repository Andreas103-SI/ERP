# inventario/models.py
from django.db import models

# Vehículo
class Vehiculo(models.Model):
    ESTADO_CHOICES = [
        ('Nuevo', 'Nuevo'),
        ('Usado', 'Usado'),
    ]
    DISPONIBILIDAD_CHOICES = [
        ('Disponible', 'Disponible'),
        ('Vendido', 'Vendido'),
    ]

    id_vehiculo = models.AutoField(primary_key=True)
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    anio = models.IntegerField()
    numero_bastidor = models.CharField(max_length=50, unique=True)
    caracteristicas = models.TextField()
    estado = models.CharField(max_length=10, choices=ESTADO_CHOICES)
    datos_propietario_anterior = models.TextField(blank=True, null=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    disponibilidad = models.CharField(max_length=15, choices=DISPONIBILIDAD_CHOICES, default='Disponible')

    def __str__(self):
        return f"{self.marca} {self.modelo} ({self.anio})"

# Inventario
class Inventario(models.Model):
    TIPO_CHOICES = [
        ('Vehículo', 'Vehículo'),
        ('Recambio', 'Recambio'),
        ('Accesorio', 'Accesorio'),
    ]

    id_inventario = models.AutoField(primary_key=True)
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES)
    vehiculo = models.ForeignKey(Vehiculo, on_delete=models.CASCADE, null=True, blank=True)
    nombre_producto = models.CharField(max_length=100, blank=True, null=True)
    cantidad = models.IntegerField()
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.tipo} - {self.nombre_producto or self.vehiculo}"

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField(default=0)
    stock_minimo = models.IntegerField(default=10)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'