from django.forms import ModelForm
from django import forms
from aplication.attention.models import CostosAtencion

# Formulario para los detalles de costos de atención
class CostoAtencionForm(ModelForm):
    class Meta:
        model = CostosAtencion
        fields = ['atencion', 'total', 'activo']  # Ajustados según los campos del modelo
        exclude = ['fecha_pago']  # Excluir campos no editables
        widgets = {
            'atencion': forms.Select(attrs={
                'class': 'form-control shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5',
                'placeholder': 'Seleccione la atención médica',
                'id': 'id_atencion',
            }),
            'total': forms.NumberInput(attrs={
                'class': 'form-control shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5',
                'placeholder': 'Ingrese el total',
                'id': 'id_total',
            }),
            'activo': forms.CheckboxInput(attrs={
                'class': 'form-checkbox h-5 w-5 text-blue-600',
                'id': 'id_activo',
            }),
        }


