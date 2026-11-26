from django.shortcuts import get_object_or_404, redirect, render

from .forms import ProntuarioForm
from .models import Prontuario


def list_prontuario(request):
    prontuarios = Prontuario.objects.select_related(
        'atendimento',
        'atendimento__animal',
    )
    return render(
        request,
        'prontuario/list_prontuario.html',
        {'prontuarios': prontuarios},
    )


def add_prontuario(request):
    if request.method == 'POST':
        form = ProntuarioForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('prontuario:list_prontuario')
    else:
        form = ProntuarioForm()

    return render(request, 'prontuario/form_prontuario.html', {'form': form})


def edit_prontuario(request, id_prontuario):
    prontuario = get_object_or_404(Prontuario, pk=id_prontuario)

    if request.method == 'POST':
        form = ProntuarioForm(
            request.POST,
            request.FILES,
            instance=prontuario,
        )
        if form.is_valid():
            form.save()
            return redirect('prontuario:list_prontuario')
    else:
        form = ProntuarioForm(instance=prontuario)

    return render(
        request,
        'prontuario/form_prontuario.html',
        {'form': form, 'prontuario': prontuario},
    )


def delete_prontuario(request, id_prontuario):
    prontuario = get_object_or_404(Prontuario, pk=id_prontuario)

    if request.method == 'POST':
        prontuario.delete()
        return redirect('prontuario:list_prontuario')

    return render(
        request,
        'prontuario/confirm_delete_prontuario.html',
        {'prontuario': prontuario},
    )
