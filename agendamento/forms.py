from django import forms
from agendamento.models import Agendamento

class AgendamentoForm(forms.ModelForm):
    class Meta:
        model = Agendamento
        exclude = ("data_registro", "usuario")
        
    descricao = forms.CharField(
        required=True,
        max_length=50,
        label="Descrição",
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
            }
        )
    )

    data_agendada = forms.DateField(
        required=True,
        label="Data",
        widget=forms.DateInput(
            format='%Y-%m-%d',
            attrs={
                "class": "form-control",
                "type": "date"
            }
        )
    )

    hora_agendada = forms.TimeField(
        required=True,
        label="Hora",
        widget=forms.TimeInput(
            attrs={
                "class": "form-control",
                "type": "time"
            }
        )
    )