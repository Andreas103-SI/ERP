# pedidos/serializers.py
from rest_framework import serializers
from .models import Pedido
from proveedores.serializers import ProveedorSerializer  # Importamos desde proveedores

class PedidoSerializer(serializers.ModelSerializer):
    proveedor = ProveedorSerializer(read_only=True)

    class Meta:
        model = Pedido
        fields = ['id_pedido', 'proveedor', 'producto', 'cantidad', 'valor', 'estado', 'iva', 'total', 'fecha_pedido']