from django import forms
from .models import Veterinario

class ClientForm(forms.ModelForm):

    class Meta:
        model = Veterinario
        exclude = ()