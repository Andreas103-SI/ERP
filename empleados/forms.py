# empleados/forms.py
from django import forms
from .models import Empleado

class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = ['nombre', 'apellido', 'dni', 'telefono', 'email', 'direccion', 'puesto', 'salario', 'fecha_contratacion']
        widgets = {
            'fecha_contratacion': forms.DateInput(attrs={'type': 'date'}),
        }