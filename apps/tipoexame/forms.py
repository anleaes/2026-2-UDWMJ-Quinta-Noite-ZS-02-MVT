from django import forms

from .models import TipoExame


class TipoExameForm(forms.ModelForm):
    class Meta:
        model = TipoExame
        fields = ('nome', 'descricao', 'valor', 'tempo_resultado')