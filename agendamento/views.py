from django.shortcuts import render
from .models import Agendamento

def index_agendamento(request):
    return render(request, 'agendamento/index_agendamento.html', {})

def lista_agendamentos(request):
    agendamentos = Agendamento.objects.all()
    context = {
        'agendamentos':agendamentos,
    }
    return render(request, 'agendamento/list.html', context)

def add_agendamento(request):
  
    return render(request, 'agendamento/add.html', {})