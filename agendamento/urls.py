from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('list/', views.lista_agendamentos, name='lista_agendamentos'),
    path('add/', views.add_agendamento, name='add_agendamento'),
]