from rest_framework import serializers
from .models import Finanzas, Gasto
from ventas.models import Venta
from pedidos.models import Pedido
from empleados.models import Empleado

class FinanzasSerializer(serializers.ModelSerializer):
    venta = serializers.PrimaryKeyRelatedField(queryset=Venta.objects.all(), required=False, allow_null=True)
    pedido = serializers.PrimaryKeyRelatedField(queryset=Pedido.objects.all(), required=False, allow_null=True)
    empleado = serializers.PrimaryKeyRelatedField(queryset=Empleado.objects.all(), required=False, allow_null=True)

    class Meta:
        model = Finanzas
        fields = '__all__'

class GastoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gasto
        fields = '__all__'