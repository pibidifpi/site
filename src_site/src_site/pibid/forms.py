from django.forms import ModelForm
from django import forms
from models import *

class ParticipanteForm(ModelForm):
    class Meta:
        model = Participante

class InscricaoForm(ModelForm):
    class Meta:
        model = Inscricao
