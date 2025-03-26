# ventas/serializers.py
from rest_framework import serializers
from .models import Cliente, Venta, VentaVehiculo
from inventario.models import Vehiculo

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ['id_cliente', 'nombre', 'apellido', 'dni_pasaporte', 'telefono', 'email', 'direccion']

class VentaVehiculoSerializer(serializers.ModelSerializer):
    venta = serializers.PrimaryKeyRelatedField(queryset=Venta.objects.all())
    vehiculo = serializers.PrimaryKeyRelatedField(queryset=Vehiculo.objects.all())

    class Meta:
        model = VentaVehiculo
        fields = ['id', 'venta', 'vehiculo']

class VentaSerializer(serializers.ModelSerializer):
    cliente = ClienteSerializer(read_only=True)
    venta_vehiculos = VentaVehiculoSerializer(many=True, read_only=True, source='ventavehiculo_set')

    class Meta:
        model = Venta
        fields = ['id_venta', 'cliente', 'presupuesto', 'contrato', 'fecha', 'valor_venta', 'iva', 'total', 'venta_vehiculos']