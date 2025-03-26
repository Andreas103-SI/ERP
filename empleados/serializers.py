# empleados/serializers.py
from rest_framework import serializers
from .models import Empleado

class EmpleadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empleado
        fields = ['id', 'nombre', 'apellido', 'dni', 'telefono', 'email', 'direccion', 'puesto', 'salario', 'fecha_contratacion']