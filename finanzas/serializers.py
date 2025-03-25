# finanzas/serializers.py
from rest_framework import serializers
from .models import Finanzas, Gasto
from ventas.models import Venta
from pedidos.models import Pedido
from empleados.models import Empleado

class FinanzasSerializer(serializers.ModelSerializer):
    venta = serializers.StringRelatedField()
    pedido = serializers.StringRelatedField()
    empleado = serializers.StringRelatedField()

    class Meta:
        model = Finanzas
        fields = ['id_finanzas', 'tipo', 'venta', 'pedido', 'empleado', 'descripcion', 'valor', 'iva', 'total', 'fecha']

class GastoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gasto
        fields = ['id', 'descripcion', 'monto', 'categoria', 'fecha', 'fecha_creacion', 'fecha_actualizacion']