from django.forms import ModelForm
from django import forms
from models import *

class ParticipanteForm(ModelForm):
    class Meta:
        model = Participante

class InscricaoForm(ModelForm):
    def __init__(self,*args,**kwargs):
        super (InscricaoForm,self ).__init__(*args,**kwargs) # populates the post
        self.fields['atividades'].queryset = Atividade.objects.filter(disponivel=True).order_by('titulo')

    class Meta:
        model = Inscricao
        fields = ['atividades']
