from django.shortcuts import get_object_or_404, redirect, render

from .forms import TipoExameForm
from .models import TipoExame


def list_tipoexame(request):
    tipoexames = TipoExame.objects.all()
    return render(
        request,
        'tipoexame/list_tipoexame.html',
        {'tipoexames': tipoexames},
    )


def add_tipoexame(request):
    if request.method == 'POST':
        form = TipoExameForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tipoexame:list_tipoexame')
    else:
        form = TipoExameForm()

    return render(request, 'tipoexame/form_tipoexame.html', {'form': form})


def edit_tipoexame(request, id_tipoexame):
    tipoexame = get_object_or_404(TipoExame, pk=id_tipoexame)

    if request.method == 'POST':
        form = TipoExameForm(request.POST, instance=tipoexame)
        if form.is_valid():
            form.save()
            return redirect('tipoexame:list_tipoexame')
    else:
        form = TipoExameForm(instance=tipoexame)

    return render(request, 'tipoexame/form_tipoexame.html', {'form': form})


def delete_tipoexame(request, id_tipoexame):
    tipoexame = get_object_or_404(TipoExame, pk=id_tipoexame)
    tipoexame.delete()
    return redirect('tipoexame:list_tipoexame')



