from django import forms
from ControlStock.models import Productos

class productosForm(forms.ModelForm):
    class Meta:
        model = Productos
        fields = [
            'id_producto',
            'producto',
            'cantidad',
            'fecha_vencimiento',
            'observacion',
]

        labels = {
            'id_producto' : 'Id producto',
            'producto': 'Producto',
            'cantidad' : 'Cantidad',
            'fecha_vencimiento' : 'Fecha de Vencimiento',
            'observacion' : 'Observacion',
        }

        widgets = {
            'id_producto' : forms.NumberInput(attrs={'class':'form-control'}),
            'producto' : forms.TextInput(attrs={'class':'form-control'}),
            'cantidad' : forms.NumberInput(attrs={'class':'form-control'}),
            'fecha_vencimiento' :forms.DateInput(attrs={'class':'form-control'}),
            'observacion' :forms.TextInput(attrs={'class':'form-control'}),
        }


class FormularioSuma(forms.Form):
    suma = forms.IntegerField()

class FormularioResta(forms.Form):
    resta = forms.IntegerField()

