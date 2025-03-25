# pedidos/forms.py
from django import forms
from .models import Pedido

class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ['cliente', 'vehiculo', 'fecha_pedido', 'estado', 'total']
        widgets = {
            'fecha_pedido': forms.DateInput(attrs={'type': 'date'}),
        }