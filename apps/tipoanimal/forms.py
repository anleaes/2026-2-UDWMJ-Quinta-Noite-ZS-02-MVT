from django import forms

from .models import TipoAnimal


class TipoAnimalForm(forms.ModelForm):
    class Meta:
        model = TipoAnimal
        fields = ('nome', 'porte', 'descricao', 'faixa_peso')
