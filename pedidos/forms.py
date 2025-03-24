# pedidos/forms.py
from django import forms
from .models import Pedido

class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ['cliente', 'vehiculo', 'proveedor', 'empleado', 'fecha', 'estado', 'total']
        