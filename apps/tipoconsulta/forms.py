from django import forms

from .models import TipoConsulta


class TipoConsultaForm(forms.ModelForm):
    class Meta:
        model = TipoConsulta
        fields = ('nome', 'descricao')
