from django.db import models
from django.conf import settings
from django.utils import timezone


class Agendamento(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    descricao = models.CharField(max_length=100)
    data_registro = models.DateTimeField(default=timezone.now)
    data_agendada = models.DateField(blank=True, null=True)
    hora_agendada = models.TimeField(blank=True, null=True)

    def get_user(self):
        return self.usuario

    def __str__(self):
        return self.descricao

    def get_data_agendada(self):
        return self.data_agendada    
