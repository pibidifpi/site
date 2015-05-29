from django.db import models

# Create your models here.

class Evento(models.Model):
    nome = models.CharField(max_length=50, verbose_name='Nome')
    local = models.CharField(max_length=100, verbose_name='Local')
    dataInicio = models.DateField(verbose_name='Data Inicio')
    dataTermino = models.DateField(verbose_name='Data Termino')
    resumo = models.TextField(verbose_name='Resumo')

    def __str__(self):
        return self.nome.encode('utf8')

class Empresa(models.Model):
    nome = models.CharField(max_length=50, verbose_name='Nome')
    logo = models.ImageField(upload_to='imagens/', verbose_name='Logo')
    valor = models.FloatField(verbose_name='Valor')
    outros = models.TextField(verbose_name='Outras Informacoes')
    evento = models.ForeignKey(Evento)

    def __str__(self):
        return self.nome.encode('utf8')

class Colaborador(models.Model):
    nome = models.CharField(max_length=50, verbose_name='Nome')
    email = models.EmailField(verbose_name='Email')
    informacoes = models.TextField(verbose_name='Informacoes')

    def __str__(self):
        return self.nome.encode('utf8')

class TipoParticipante(models.Model):
    nome = models.CharField(max_length=50, verbose_name='Nome')

    def __str__(self):
        return self.nome.encode('utf8')


class TipoAtividade(models.Model):
    nome = models.CharField(max_length=50, verbose_name='Nome')

    def __str__(self):
        return self.nome.encode('utf8')

class Atividade(models.Model):
    titulo = models.CharField(max_length=255, verbose_name='Titulo')
    duracao = models.CharField(max_length=10, verbose_name='Duracao')
    quantidadeVagas = models.IntegerField(verbose_name='Quantidade de Vagas')
    dataInicio = models.DateField(verbose_name='Data Inicio')
    dataTermino = models.DateField(verbose_name='Data Termino')
    horario = models.CharField(max_length=10, verbose_name='Horario')
    resumo = models.TextField(verbose_name='Resumo')
    tipo = models.ForeignKey(TipoAtividade)
    evento = models.ForeignKey(Evento)
    colaborador = models.ForeignKey(Colaborador)

    def __str__(self):
        return self.titulo.encode('utf8')

class Preco(models.Model):
    normal = models.FloatField(max_length=50, verbose_name='Normal (R$)')
    tipo = models.ForeignKey(TipoParticipante)
    atividade = models.ForeignKey(Atividade)

    def __str__(self):
        return str(self.normal).encode('utf8')

class Participante(models.Model):
    nome = models.CharField(max_length=50, verbose_name='Nome')
    cpf = models.CharField(max_length=14, verbose_name='CPF')
    email = models.EmailField(verbose_name='Email')
    origem = models.CharField(max_length=50, verbose_name='Origem')
    tipo = models.ForeignKey(TipoParticipante)

    def __str__(self):
        return self.nome.encode('utf8')

class Inscricao(models.Model):
    data = models.DateTimeField(auto_now=True)
    participante = models.ForeignKey(Participante)
    atividades = models.ManyToManyField(Atividade)

    def __str__(self):
        return str(self.id).encode('utf8')