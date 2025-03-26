# finanzas/forms.py
from django import forms
from .models import Finanzas, Gasto

class FinanzasForm(forms.ModelForm):
    class Meta:
        model = Finanzas
        fields = ['tipo', 'descripcion', 'venta', 'pedido', 'empleado', 'valor', 'iva', 'total', 'fecha']
        widgets = {
            'tipo': forms.Select(attrs={'class': 'form-select'}),
            'fecha': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'venta': forms.Select(attrs={'class': 'form-select'}),  # Debe ser Select, no NumberInput
            'pedido': forms.Select(attrs={'class': 'form-select'}),
            'empleado': forms.Select(attrs={'class': 'form-select'}),
            'valor': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'iva': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'total': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
        }

class GastoForm(forms.ModelForm):
    class Meta:
        model = Gasto
        fields = ['descripcion', 'monto', 'categoria', 'fecha']
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'monto': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'categoria': forms.Select(attrs={'class': 'form-select'}),
        }