# ventas/serializers.py
from rest_framework import serializers
from .models import Cliente, Venta, VentaVehiculo
from inventario.models import Vehiculo

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ['id_cliente', 'nombre', 'apellido', 'dni_pasaporte', 'telefono', 'email', 'direccion']

class VentaSerializer(serializers.ModelSerializer):
    cliente = ClienteSerializer(read_only=True)

    class Meta:
        model = Venta
        fields = ['id_venta', 'cliente', 'presupuesto', 'contrato', 'fecha', 'valor_venta', 'iva', 'total']

class VentaVehiculoSerializer(serializers.ModelSerializer):
    venta = VentaSerializer(read_only=True)
    vehiculo = serializers.StringRelatedField()

    class Meta:
        model = VentaVehiculo
        fields = ['venta', 'vehiculo']