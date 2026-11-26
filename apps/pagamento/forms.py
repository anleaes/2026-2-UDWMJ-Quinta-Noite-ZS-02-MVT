from django import forms

from .models import Pagamento


class PagamentoForm(forms.ModelForm):
    class Meta:
        model = Pagamento
        fields = (
            'atendimento',
            'valor_total',
            'forma_pagamento',
            'status_pagamento',
            'data_pagamento',
        )
        widgets = {
            'data_pagamento': forms.DateTimeInput(
                attrs={'type': 'datetime-local'},
                format='%Y-%m-%dT%H:%M',
            ),
        }
