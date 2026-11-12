from django.shortcuts import render, get_object_or_404, redirect
from .forms import EspecialidadeForm
from .models import Especialidade

# Create your views here.
def add_especialidade(request):
    template_name = 'especialidade/add_especialidade.html'
    context = {}
    if request.method == 'POST':
        form = EspecialidadeForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            form.save_m2m()
            return redirect('especialidade:list_especialidades')
    form = EspecialidadeForm()
    context['form'] = form
    return render(request, template_name, context)

def list_especialidade(request):
    template_name = 'especialidade/list_especialidade.html'
    especialidade = Especialidade.objects.filter()
    context = {
        'especialidade': especialidade
    }
    return render(request, template_name, context)

def edit_especialidade(request, id_especialidade):
    template_name = 'especialidade/add_especialidade.html'
    context ={}
    especialidade = get_object_or_404(Especialidade, id=id_especialidade)
    if request.method == 'POST':
        form = EspecialidadeForm(request.POST, instance=especialidade)
        if form.is_valid():
            form.save()
            return redirect('especialidade:list_especialidades')
    form = EspecialidadeForm(instance=especialidade)
    context['form'] = form
    return render(request, template_name, context)

def delete_especialidade(request, id_especialidade):
    especialidade = Especialidade.objects.get(id=id_especialidade)
    especialidade.delete()
    return redirect('especialidade:list_especialidade')
