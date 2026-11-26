from django import forms

from .models import Prontuario


class ProntuarioForm(forms.ModelForm):
    class Meta:
        model = Prontuario
        fields = (
            'descricao',
            'diagnostico',
            'prescricao',
            'data_registro',
            'atendimento',
        )
        widgets = {
            'data_registro': forms.DateInput(attrs={'type': 'date'}),
        }
