from django import forms

from .models import Atendimento


class AtendimentoForm(forms.ModelForm):
    class Meta:
        model = Atendimento
        fields = (
            'data_hora',
            'motivo',
            'observacoes',
            'status',
            'tipo_atendimento',
            'animal',
            'veterinario',
        )
        widgets = {
            'data_hora': forms.DateTimeInput(
                attrs={'type': 'datetime-local'},
                format='%Y-%m-%dT%H:%M',
            ),
        }
