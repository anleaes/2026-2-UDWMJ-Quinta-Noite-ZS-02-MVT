from django.shortcuts import get_object_or_404, redirect, render

from .forms import TipoAnimalForm
from .models import TipoAnimal


def list_tipoanimal(request):
    tipoanimais = TipoAnimal.objects.all()
    return render(
        request,
        'tipoanimal/list_tipoanimal.html',
        {'tipoanimais': tipoanimais},
    )


def add_tipoanimal(request):
    if request.method == 'POST':
        form = TipoAnimalForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tipoanimal:list_tipoanimal')
    else:
        form = TipoAnimalForm()

    return render(request, 'tipoanimal/form_tipoanimal.html', {'form': form})


def edit_tipoanimal(request, id_tipoanimal):
    tipoanimal = get_object_or_404(TipoAnimal, pk=id_tipoanimal)
    if request.method == 'POST':
        form = TipoAnimalForm(request.POST, instance=tipoanimal)
        if form.is_valid():
            form.save()
            return redirect('tipoanimal:list_tipoanimal')
    else:
        form = TipoAnimalForm(instance=tipoanimal)

    return render(request, 'tipoanimal/form_tipoanimal.html', {'form': form})


def delete_tipoanimal(request, id_tipoanimal):
    tipoanimal = get_object_or_404(TipoAnimal, pk=id_tipoanimal)
    tipoanimal.delete()
    return redirect('tipoanimal:list_tipoanimal')
