from django import forms

from .models import AtendimentoExame


class AtendimentoExameForm(forms.ModelForm):
    class Meta:
        model = AtendimentoExame
        fields = (
            'atendimento',
            'tipo_exame',
            'resultado',
            'data_realizacao',
        )
        widgets = {
            'data_realizacao': forms.DateTimeInput(
                attrs={'type': 'datetime-local'},
                format='%Y-%m-%dT%H:%M',
            ),
        }
