from rest_framework import serializers
from .models import Cliente, Venta, VentaVehiculo

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

class VentaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Venta
        fields = '__all__'

class VentaVehiculoSerializer(serializers.ModelSerializer):
    class Meta:
        model = VentaVehiculo
        fields = '__all__'