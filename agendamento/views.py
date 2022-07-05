from multiprocessing import context
from django.shortcuts import redirect, render
from agendamento.forms import AgendamentoForm
from .models import Agendamento

# Pagina inicial de agendamentos
def index_agendamento(request):
    return render(request, "agendamento/index_agendamento.html", {})


# Lista agendamentos realizados
def lista_agendamentos(request):
    agendamentos = Agendamento.objects.all().order_by('data_registro')

    context = {
        "agendamentos": agendamentos,
    }
    return render(request, "agendamento/list.html", context)


# Adiciona novos agendamentos
def add_agendamento(request):
    form = AgendamentoForm(request.POST or None)
    
    if request.method == "POST":
        if form.is_valid():
            obj = form.save(commit=False)
            obj.usuario = request.user
            obj.save()
            return redirect("lista_agendamentos")
    
    context = {
        "form": form
    }
    return render(request, "agendamento/add.html", context)


# Edita agendamento cadastrado
def edit_agendamento(request, agendamento_pk):
    agendamento = Agendamento.objects.get(pk=agendamento_pk)
    form = AgendamentoForm(request.POST or None, instance=agendamento)

    if request.method == "POST":
        if form.is_valid():
            obj = form.save(commit=False)
            obj.usuario = request.user
            obj.save()
            return redirect("lista_agendamentos")

    context = {
        "form": form
    }
    return render(request, "agendamento/add.html", context)