__author__ = 'charles'

from django.shortcuts import render_to_response

def eventoIndex(request):
	return render_to_response ('lista_evento.html',locals())


def eventoSobre(request):
	return render_to_response ('sobre_evento.html',locals())
