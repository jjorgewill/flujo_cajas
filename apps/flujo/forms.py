from django import forms

from apps.flujo.models import Activo, Obligaciones


class FrmActivo(forms.ModelForm):

    class Meta:
        model = Activo
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

class FrmObligacion(forms.ModelForm):

    class Meta:
        model = Obligaciones
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'