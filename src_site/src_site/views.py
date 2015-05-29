__author__ = 'charles'

from pibid.models import *
from django.views import generic

class EventoList(generic.ListView):
    model = Evento
    queryset = Evento.objects.filter(id=1)
    template_name = "lista_evento.html"

class EventoSobre(generic.ListView):
    model = Evento
    queryset = Evento.objects.filter(id=1)
    template_name = "sobre_evento.html"

class PalestraList(generic.ListView):
    model = Atividade
    #necessario comentar as duas proximas linhas enquanto Palestra nao existir no banco
    tipoPaletra = TipoAtividade.objects.get(nome="Palestra")
    queryset = Atividade.objects.filter(tipo=tipoPaletra)
    template_name = "lista_atividade.html"
    
class MinicursoList(generic.ListView):
    model = Atividade
    #necessario comentar as duas proximas linhas enquanto Minicurso nao existir no banco
    tipoMinicurso = TipoAtividade.objects.get(nome="Minicurso")
    queryset = Atividade.objects.filter(tipo=tipoMinicurso)
    template_name = "lista_atividade.html"
