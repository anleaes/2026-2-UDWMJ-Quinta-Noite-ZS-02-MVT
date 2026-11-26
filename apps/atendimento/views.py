from django.shortcuts import get_object_or_404, redirect, render

from .forms import AtendimentoForm
from .models import Atendimento


def list_atendimento(request):
    atendimentos = Atendimento.objects.select_related(
        'tipo_consulta',
        'animal',
        'veterinario',
    )
    return render(
        request,
        'atendimento/list_atendimento.html',
        {'atendimentos': atendimentos},
    )


def add_atendimento(request):
    if request.method == 'POST':
        form = AtendimentoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('atendimento:list_atendimento')
    else:
        form = AtendimentoForm()

    return render(
        request,
        'atendimento/form_atendimento.html',
        {'form': form},
    )


def edit_atendimento(request, id_atendimento):
    atendimento = get_object_or_404(Atendimento, pk=id_atendimento)
    if request.method == 'POST':
        form = AtendimentoForm(request.POST, instance=atendimento)
        if form.is_valid():
            form.save()
            return redirect('atendimento:list_atendimento')
    else:
        form = AtendimentoForm(instance=atendimento)

    return render(
        request,
        'atendimento/form_atendimento.html',
        {'form': form, 'atendimento': atendimento},
    )


def delete_atendimento(request, id_atendimento):
    atendimento = get_object_or_404(Atendimento, pk=id_atendimento)
    atendimento.delete()
    return redirect('atendimento:list_atendimento')
