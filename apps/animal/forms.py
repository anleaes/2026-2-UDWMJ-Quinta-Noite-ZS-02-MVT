from django import forms

from .models import Animal


class AnimalForm(forms.ModelForm):
    class Meta:
        model = Animal
        fields = (
            'nome',
            'data_nascimento',
            'responsavel',
            'tipo_animal',
            'sexo',
            'foto_animal',
        )
        widgets = {
            'data_nascimento': forms.DateInput(attrs={'type': 'date'}),
        }
