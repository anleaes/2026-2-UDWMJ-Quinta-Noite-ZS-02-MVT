from django.contrib import messages
from django.db.models import ProtectedError
from django.shortcuts import get_object_or_404, redirect, render

from .forms import TipoConsultaForm
from .models import TipoConsulta


def list_tipo_consulta(request):
    tipos_consulta = TipoConsulta.objects.all()
    return render(
        request,
        'tipoconsulta/list_tipo_consulta.html',
        {'tipos_consulta': tipos_consulta},
    )


def add_tipo_consulta(request):
    if request.method == 'POST':
        form = TipoConsultaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tipoconsulta:list_tipo_consulta')
    else:
        form = TipoConsultaForm()

    return render(request, 'tipoconsulta/form_tipo_consulta.html', {'form': form})


def edit_tipo_consulta(request, id_tipo_consulta):
    tipo_consulta = get_object_or_404(TipoConsulta, pk=id_tipo_consulta)

    if request.method == 'POST':
        form = TipoConsultaForm(request.POST, instance=tipo_consulta)
        if form.is_valid():
            form.save()
            return redirect('tipoconsulta:list_tipo_consulta')
    else:
        form = TipoConsultaForm(instance=tipo_consulta)

    return render(
        request,
        'tipoconsulta/form_tipo_consulta.html',
        {'form': form, 'tipo_consulta': tipo_consulta},
    )


def delete_tipo_consulta(request, id_tipo_consulta):
    tipo_consulta = get_object_or_404(TipoConsulta, pk=id_tipo_consulta)

    if request.method == 'POST':
        try:
            tipo_consulta.delete()
        except ProtectedError:
            messages.error(
                request,
                'Não é possível excluir um tipo de consulta associado a atendimentos.',
            )
        return redirect('tipoconsulta:list_tipo_consulta')

    return render(
        request,
        'tipoconsulta/confirm_delete_tipo_consulta.html',
        {'tipo_consulta': tipo_consulta},
    )
