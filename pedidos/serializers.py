from rest_framework import serializers
from .models import Pedido

class PedidoSerializer(serializers.ModelSerializer):
    proveedor = serializers.StringRelatedField()

    class Meta:
        model = Pedido
        fields = ['id_pedido', 'proveedor', 'producto', 'cantidad', 'valor', 'estado', 'iva', 'total']