from django import forms
from agendamento.models import Agendamento

class AgendamentoForm(forms.ModelForm):
    class Meta:
        model = Agendamento
        exclude = ()
        
        widgets = {
            'descricao': forms.TextInput(attrs={'class':'form-control'}),
            'data_agendament': forms.DateTimeInput(attrs={'class':'form-control'})
        }