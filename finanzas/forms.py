# finanzas/forms.py
from django import forms
from .models import Finanzas, Gasto

class FinanzasForm(forms.ModelForm):
    class Meta:
        model = Finanzas
        fields = ['tipo', 'venta', 'pedido', 'empleado', 'descripcion', 'valor', 'iva', 'total', 'fecha']
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date'}),
        }

class GastoForm(forms.ModelForm):
    class Meta:
        model = Gasto
        fields = ['descripcion', 'monto', 'categoria', 'fecha']
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date'}),
        }