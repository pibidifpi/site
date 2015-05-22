from django.contrib import admin
from src_site.pibid.models import Empresa, Evento

# Register your models here.

class EmpresaAdmin(admin.ModelAdmin):
	model = Empresa
	list_display = ['nome','valor','outros']
	search_fields = ['nome','valor','outros']
admin.site.register(Empresa, EmpresaAdmin)

class EventoAdmin(admin.ModelAdmin):
	model = Evento
	list_display = ['nome','local','dataInicio','dataTermino','resumo']
	search_fields = ['nome','local','dataInicio','dataTermino','resumo']
admin.site.register(Evento, EventoAdmin)
