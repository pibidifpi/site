__author__ = 'charles'

from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext
from pibid.models import *
from pibid.forms import *
from django.views import generic
from django.core.urlresolvers import reverse
#from django.http import HttpResponse #usado para debugar uma variavel

class EventoList(generic.ListView):
    model = Evento
    queryset = Evento.objects.filter(id=1)
    template_name = "lista_evento.html"

class EventoDetailView(generic.DetailView):
    model = Evento
    template_name = "detalhe_evento.html"

class PalestraList(generic.ListView):
    model = Atividade
    #necessario comentar as duas proximas linhas enquanto Palestra nao existir no banco
    tipoPaletra = TipoAtividade.objects.get(nome="Palestra")
    queryset = Atividade.objects.filter(tipo=tipoPaletra)
    template_name = "lista_palestra.html"
    
class MinicursoList(generic.ListView):
    model = Atividade
    #necessario comentar as duas proximas linhas enquanto Minicurso nao existir no banco
    tipoMinicurso = TipoAtividade.objects.get(nome="Minicurso")
    queryset = Atividade.objects.filter(tipo=tipoMinicurso)
    template_name = "lista_minicurso.html"

def precoList(request, atividade_id):
    atividadeEnviada = get_object_or_404(Atividade, id=atividade_id)
    object_list = Preco.objects.filter(atividade=atividadeEnviada)
    return render_to_response('lista_preco.html',locals(), context_instance=RequestContext(request))
#return HttpResponse(html) #usado para debugar uma variavel

def setaParticipante(request):
    if request.method=='POST':
        formulario = ParticipanteForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect(reverse('setaAtividades'))
    else:
        formulario = ParticipanteForm()
    return render_to_response('seta_participante.html',locals(), context_instance=RequestContext(request))

def setaAtividades(request):
    if request.method=='POST':
        formulario = InscricaoForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect('/concluida')
    else:
        formulario = InscricaoForm()
    return render_to_response('seta_atividades.html',locals(), context_instance=RequestContext(request))

def inscricaoConcluida(request):
    return render_to_response('inscricao_concluida.html',locals(), context_instance=RequestContext(request))

