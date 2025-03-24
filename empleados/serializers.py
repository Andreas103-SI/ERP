# empleados/serializers.py
from rest_framework import serializers
from .models import Empleado

class EmpleadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empleado
        fields = ['id_empleado', 'nombre', 'apellido', 'dni', 'telefono', 'email', 'puesto', 'salario']