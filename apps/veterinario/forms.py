from django import forms
from .models import Veterinario

class VeterinarioForm(forms.ModelForm):

    class Meta:
        model = Veterinario
        exclude = ()