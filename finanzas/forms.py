# finanzas/forms.py
from django import forms
from .models import Finanzas, Gasto

class FinanzasForm(forms.ModelForm):  # Renombramos a FinanzasForm para consistencia
    class Meta:
        model = Finanzas
        fields = ['tipo', 'descripcion', 'venta', 'iva', 'total', 'fecha']  # Cambiamos monto por venta, y añadimos iva y total
        widgets = {
            'tipo': forms.Select(attrs={'class': 'form-select'}),
            'fecha': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'venta': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),  # Cambiamos valor por venta
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
            'categoria': forms.TextInput(attrs={'class': 'form-control'}),
        }