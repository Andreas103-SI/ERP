# inventario/forms.py
from django import forms
from .models import Vehiculo

class VehiculoForm(forms.ModelForm):
    class Meta:
        model = Vehiculo
        fields = ['marca', 'modelo', 'anio', 'numero_bastidor', 'caracteristicas', 'estado', 'datos_propietario_anterior', 'precio', 'disponibilidad']
        