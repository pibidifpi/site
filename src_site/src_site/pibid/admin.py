from django.contrib import admin
from src_site.pibid.models import Empresa, Evento, Colaborador, Preco, TipoParticipante, Participante, TipoAtividade, \
    Atividade, Inscricao

# Register your models here.

class EmpresaAdmin(admin.ModelAdmin):
    model = Empresa
    list_display = ['nome', 'valor', 'outros']
    search_fields = ['nome', 'valor', 'outros']
admin.site.register(Empresa, EmpresaAdmin)


class EventoAdmin(admin.ModelAdmin):
    model = Evento
    list_display = ['nome', 'local', 'dataInicio', 'dataTermino', 'resumo']
    search_fields = ['nome', 'local', 'dataInicio', 'dataTermino', 'resumo']
admin.site.register(Evento, EventoAdmin)


class ColaboradorAdmin(admin.ModelAdmin):
    model = Colaborador
    list_display = ['nome', 'email', 'informacoes']
    search_fields = ['nome', 'email', 'informacoes']
admin.site.register(Colaborador, ColaboradorAdmin)


class PrecoAdmin(admin.ModelAdmin):
    model = Preco
    list_display = ['normal', 'desconto']
    search_fields = ['normal', 'desconto']
admin.site.register(Preco, PrecoAdmin)


class TipoParticipanteAdmin(admin.ModelAdmin):
    model = TipoParticipante
    list_display = ['nome']
    search_fields = ['nome']
admin.site.register(TipoParticipante, TipoParticipanteAdmin)


class ParticipanteAdmin(admin.ModelAdmin):
    model = Participante
    list_display = ['nome', 'cpf', 'email', 'origem', 'tipo']
    list_filter = ['tipo__nome']
    search_fields = ['nome', 'cpf', 'email', 'origem', 'tipo__nome']
admin.site.register(Participante, ParticipanteAdmin)


class TipoAtividadeAdmin(admin.ModelAdmin):
    model = TipoAtividade
    list_display = ['nome']
    search_fields = ['nome']
admin.site.register(TipoAtividade, TipoAtividadeAdmin)


class AtividadeAdmin(admin.ModelAdmin):
    model = Atividade
    list_display = ['descricao', 'duracao', 'quantidadeVagas', 'dataInicio', 'dataTermino', 'horario', 'tipo', 'evento']
    list_filter = ['tipo__nome', 'evento__nome']
    search_fields = ['descricao', 'duracao', 'quantidadeVagas', 'dataInicio', 'dataTermino', 'horario', 'tipo__nome',
                 'evento__nome']
admin.site.register(Atividade, AtividadeAdmin)


class InscricaoAdmin(admin.ModelAdmin):
    model = Inscricao
    list_display = ['data', 'participante']
    search_fields = ['data', 'participante__nome']
admin.site.register(Inscricao, InscricaoAdmin)
