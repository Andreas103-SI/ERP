# finanzas/forms.py
from django import forms
from .models import Finanzas

class FinanzasForm(forms.ModelForm):
    class Meta:
        model = Finanzas
        fields = ['descripcion', 'valor', 'total', 'tipo', 'fecha', 'empleado']