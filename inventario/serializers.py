# inventario/serializers.py
from rest_framework import serializers
from .models import Vehiculo

class VehiculoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehiculo
        fields = ['id_vehiculo', 'marca', 'modelo', 'anio', 'numero_bastidor', 'caracteristicas', 'estado', 'datos_propietario_anterior', 'precio', 'disponibilidad']