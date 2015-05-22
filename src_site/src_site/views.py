__author__ = 'charles'

import datetime
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from pibid.models import Evento
#from django.http import HttpResponse #usado para debugar uma variavel

def eventoIndex(request):
    """
    a funcao
    filter(dataInicio__lte=datetime.date.today(), dataTermino__gt=datetime.date.today())[:1]
    faz a seguinte consulta no banco de dados
    SELECT * from pibid_evento WHERE (dataInicio >= 'hoje' AND dataTermino < 'hoje') LIMIT 1
    """
    evento = Evento.objects.filter(dataInicio__lte=datetime.date.today(), dataTermino__gt=datetime.date.today())[:1]
    return render_to_response('lista_evento.html',locals(), context_instance=RequestContext(request))


def eventoSobre(request):
    evento = Evento.objects.filter(dataInicio__lte=datetime.date.today(), dataTermino__gt=datetime.date.today())[:1]
    #return HttpResponse(str(dado.resumo)) #usado para debugar uma variavel
    return render_to_response('sobre_evento.html',locals(), context_instance=RequestContext(request))

