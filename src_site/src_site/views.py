__author__ = 'charles'

from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext
from pibid.models import *
from pibid.forms import *
from django.views import generic
from django.core.urlresolvers import reverse
from django.http import HttpResponse #usado para debugar uma variavel

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

# funcoes utilizadas no passo a passo da inscricao
def novaInscricao(request):
    titlePagina = 'Informe os dados do participante'
    divPorcentagem = 25
    spanPorcentagem = 25
    abaAtiva = 'aba-participante'

    tipo_id = "1" #valor padrao para quando o valor for nulo
    if request.POST.get('tipo'):
        tipo_id = request.POST.get('tipo')

    tipoEnviado = get_object_or_404(TipoParticipante, id=tipo_id)
    precos = Preco.objects.filter(tipo=tipoEnviado)

    if request.POST.get('etapa')=='1' or request.POST.get('etapa')=='4':
        return setaParticipante(request, precos) #valida dados do formulario dados do participante
    elif request.POST.get('etapa')=='2' or request.POST.get('etapa')=='5':
        return setaAtividades(request, precos) # valida dados do formulario das atividades
    elif request.POST.get('etapa')=='3':
        return confirmaInscricao(request, precos) # confirma os dados de inscricao
    else:
        formParticipante = ParticipanteForm()
        formInscricao = InscricaoForm()
    #cria formulario dados do participante em branco
    return render_to_response('nova_inscricao.html',locals(), context_instance=RequestContext(request))

def setaParticipante(request, precos):
    titlePagina = 'Informe os dados do participante'
    divPorcentagem = 25
    spanPorcentagem = 25
    abaAtiva = 'aba-participante'

    formParticipante = ParticipanteForm(request.POST)

    if request.POST.get('atividades'):
        formInscricao = InscricaoForm(request.POST)
    else:
        formInscricao = InscricaoForm()

    #o request.POST.get('etapa') eh igual a '4' quando a pessoa clica no botao voltar p/ participante
    if formParticipante.is_valid() and request.POST.get('etapa')!='4':
        titlePagina = 'Informe as atividades'
        divPorcentagem = 50
        spanPorcentagem = 50
        abaAtiva = 'aba-atividades'
    return render_to_response('nova_inscricao.html',locals(), context_instance=RequestContext(request))

def setaAtividades(request, precos):
    titlePagina = 'Informe as atividades'
    divPorcentagem = 50
    spanPorcentagem = 50
    abaAtiva = 'aba-atividades'

    formParticipante = ParticipanteForm(request.POST)
    formInscricao = InscricaoForm(request.POST)
    #o request.POST.get('etapa') eh igual a '5' quando a pessoa clica no botao voltar p/ atividades
    if request.POST.get('atividades') and request.POST.get('etapa')!='5':
        titlePagina = 'Confirme os dados'
        divPorcentagem = 75
        spanPorcentagem = 75
        abaAtiva = 'aba-confirmacao'
    return render_to_response('nova_inscricao.html',locals(), context_instance=RequestContext(request))

def atualizaInscritosAtividade(atividades):
    #logica para fazer o controle das vagas por atividade
    for atividade_id in atividades:
        atividade = Atividade.objects.get(id=atividade_id)
        atividade.quantidadeInscritos = atividade.quantidadeInscritos + 1

        if atividade.quantidadeInscritos >= atividade.quantidadeVagas:
           atividade.disponivel = False

        atividade.save()
    #fim logica do controle de vagas

def confirmaInscricao(request, precos):
    titlePagina = 'Confirme os dados'
    divPorcentagem = 75
    spanPorcentagem = 75
    abaAtiva = 'aba-confirmacao'

    formParticipante = ParticipanteForm(request.POST)
    formInscricao = InscricaoForm(request.POST)

    if formParticipante.is_valid() and formInscricao.is_valid():
        novoParticipante = formParticipante.save()
        nInscricao = formInscricao.save(commit=False)
        nInscricao.participante = novoParticipante
        nInscricao.save()
        formInscricao.save_m2m() #save the many-to-many data for the form.

        atualizaInscritosAtividade(request.POST.getlist('atividades'))

        return HttpResponseRedirect(reverse('inscricaoConcluida'))

    return render_to_response('nova_inscricao.html',locals(), context_instance=RequestContext(request))

def inscricaoConcluida(request):
    return render_to_response('inscricao_concluida.html',locals(), context_instance=RequestContext(request))
# fim do passo a passo da inscricao
