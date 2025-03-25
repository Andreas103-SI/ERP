# inventario/serializers.py
from rest_framework import serializers
from .models import Vehiculo

class VehiculoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehiculo
        fields = ['id', 'marca', 'modelo', 'anio', 'precio', 'categoria', 'stock']