from django.shortcuts import get_object_or_404, redirect, render

from .forms import AnimalForm
from .models import Animal


def list_animal(request):
    animais = Animal.objects.select_related('responsavel', 'tipo_animal')
    return render(request, 'animal/list_animal.html', {'animais': animais})


def add_animal(request):
    if request.method == 'POST':
        form = AnimalForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('animal:list_animal')
    else:
        form = AnimalForm()

    return render(request, 'animal/form_animal.html', {'form': form})


def edit_animal(request, id_animal):
    animal = get_object_or_404(Animal, pk=id_animal)
    if request.method == 'POST':
        form = AnimalForm(request.POST, request.FILES, instance=animal)
        if form.is_valid():
            form.save()
            return redirect('animal:list_animal')
    else:
        form = AnimalForm(instance=animal)

    return render(request, 'animal/form_animal.html', {'form': form, 'animal': animal})


def delete_animal(request, id_animal):
    animal = get_object_or_404(Animal, pk=id_animal)
    animal.delete()
    return redirect('animal:list_animal')
