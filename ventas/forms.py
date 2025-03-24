# ventas/forms.py
from django import forms
from .models import Cliente, Venta, VentaVehiculo

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre', 'apellido', 'dni_pasaporte', 'telefono', 'email', 'direccion']

class VentaForm(forms.ModelForm):
    class Meta:
        model = Venta
        fields = ['cliente', 'presupuesto', 'contrato', 'fecha', 'valor_venta', 'iva', 'total']
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date'}),
        }

class VentaVehiculoForm(forms.ModelForm):
    class Meta:
        model = VentaVehiculo
        fields = ['venta', 'vehiculo']