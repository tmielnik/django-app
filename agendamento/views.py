from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse
from .models import Agendamento

def lista_agendamentos(request):
    agendamentos = Agendamento.objects.all()
    context = {
        'agendamentos':agendamentos,
    }
    return render(request, 'agendamento/list.html', context)

def add_agendamento(request):
  
    return render(request, 'agendamento/add.html', {})