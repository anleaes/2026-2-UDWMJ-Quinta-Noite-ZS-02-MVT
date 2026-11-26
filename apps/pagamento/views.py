from django.shortcuts import get_object_or_404, redirect, render

from .forms import PagamentoForm
from .models import Pagamento


def list_pagamento(request):
    pagamentos = Pagamento.objects.select_related(
        'atendimento',
        'atendimento__animal',
    )
    return render(
        request,
        'pagamento/list_pagamento.html',
        {'pagamentos': pagamentos},
    )


def add_pagamento(request):
    if request.method == 'POST':
        form = PagamentoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pagamento:list_pagamento')
    else:
        form = PagamentoForm()

    return render(request, 'pagamento/form_pagamento.html', {'form': form})


def edit_pagamento(request, id_pagamento):
    pagamento = get_object_or_404(Pagamento, pk=id_pagamento)

    if request.method == 'POST':
        form = PagamentoForm(request.POST, instance=pagamento)
        if form.is_valid():
            form.save()
            return redirect('pagamento:list_pagamento')
    else:
        form = PagamentoForm(instance=pagamento)

    return render(
        request,
        'pagamento/form_pagamento.html',
        {'form': form, 'pagamento': pagamento},
    )


def delete_pagamento(request, id_pagamento):
    pagamento = get_object_or_404(Pagamento, pk=id_pagamento)

    if request.method == 'POST':
        pagamento.delete()
        return redirect('pagamento:list_pagamento')

    return render(
        request,
        'pagamento/confirm_delete_pagamento.html',
        {'pagamento': pagamento},
    )
