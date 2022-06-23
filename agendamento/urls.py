from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_agendamento, name='index_agendamento'),
    path('list/', views.lista_agendamentos, name='lista_agendamentos'),
    path('add/', views.add_agendamento, name='add_agendamento'),
]