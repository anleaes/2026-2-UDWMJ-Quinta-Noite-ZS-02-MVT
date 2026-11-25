from django.shortcuts import get_object_or_404, redirect, render

from .forms import AtendimentoExameForm
from .models import AtendimentoExame


def list_atendimentoexame(request):
    atendimentoexames = AtendimentoExame.objects.select_related(
        'atendimento',
        'tipo_exame',
    )
    return render(
        request,
        'atendimentoexame/list_atendimentoexame.html',
        {'atendimentoexames': atendimentoexames},
    )


def add_atendimentoexame(request):
    if request.method == 'POST':
        form = AtendimentoExameForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('atendimentoexame:list_atendimentoexame')
    else:
        form = AtendimentoExameForm()

    return render(
        request,
        'atendimentoexame/form_atendimentoexame.html',
        {'form': form},
    )


def edit_atendimentoexame(request, id_atendimentoexame):
    atendimentoexame = get_object_or_404(
        AtendimentoExame,
        pk=id_atendimentoexame,
    )
    if request.method == 'POST':
        form = AtendimentoExameForm(request.POST, instance=atendimentoexame)
        if form.is_valid():
            form.save()
            return redirect('atendimentoexame:list_atendimentoexame')
    else:
        form = AtendimentoExameForm(instance=atendimentoexame)

    return render(
        request,
        'atendimentoexame/form_atendimentoexame.html',
        {'form': form, 'atendimentoexame': atendimentoexame},
    )


def delete_atendimentoexame(request, id_atendimentoexame):
    atendimentoexame = get_object_or_404(
        AtendimentoExame,
        pk=id_atendimentoexame,
    )
    atendimentoexame.delete()
    return redirect('atendimentoexame:list_atendimentoexame')
