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

    class Meta:
        ordering = ["nome"]


Evento.objects.order_by('nome')

class Empresa(models.Model):
    nome = models.CharField(max_length=50, verbose_name='Nome')
    logo = models.ImageField(upload_to='imagens/', verbose_name='Logo')
    valor = models.FloatField(verbose_name='Valor')
    outros = models.TextField(verbose_name='Outras Informacoes')
    evento = models.ForeignKey(Evento)

    def __str__(self):
        return self.nome.encode('utf8')

    class Meta:
        ordering = ["nome"]

class Colaborador(models.Model):
    nome = models.CharField(max_length=50, verbose_name='Nome')
    email = models.EmailField(verbose_name='Email', unique=True)
    informacoes = models.TextField(verbose_name='Informacoes')

    def __str__(self):
        return self.nome.encode('utf8')

    class Meta:
        ordering = ["nome"]

class TipoParticipante(models.Model):
    nome = models.CharField(max_length=50, verbose_name='Nome')

    def __str__(self):
        return self.nome.encode('utf8')

    class Meta:
        ordering = ["nome"]


class TipoAtividade(models.Model):
    nome = models.CharField(max_length=50, verbose_name='Nome')

    def __str__(self):
        return self.nome.encode('utf8')

    class Meta:
        ordering = ["nome"]

class Atividade(models.Model):
    titulo = models.CharField(max_length=255, verbose_name='Titulo')
    duracao = models.CharField(max_length=10, verbose_name='Duracao')
    quantidadeInscritos = models.IntegerField(editable=False, default=0)
    quantidadeVagas = models.IntegerField(verbose_name='Quantidade de Vagas')
    disponivel = models.BooleanField(editable=False, default=True)
    dataInicio = models.DateField(verbose_name='Data Inicio')
    dataTermino = models.DateField(verbose_name='Data Termino')
    horario = models.CharField(max_length=10, verbose_name='Horario')
    resumo = models.TextField(verbose_name='Resumo')
    tipo = models.ForeignKey(TipoAtividade)
    evento = models.ForeignKey(Evento)
    colaborador = models.ForeignKey(Colaborador)
    material = models.FileField(upload_to='material_atividades/', verbose_name='Material', blank=True)

    def __str__(self):
        return self.titulo.encode('utf8')

    class Meta:
        ordering = ["titulo"]

class Preco(models.Model):
    normal = models.FloatField(max_length=50, verbose_name='Normal (R$)')
    tipo = models.ForeignKey(TipoParticipante)
    atividade = models.ForeignKey(Atividade)

    def __str__(self):
        return str(self.normal).encode('utf8')

    class Meta:
        ordering = ["id"]

class Participante(models.Model):
    nome = models.CharField(max_length=50, verbose_name='Nome')
    cpf = models.CharField(max_length=14, verbose_name='CPF')
    email = models.EmailField(verbose_name='E-mail', unique=True)
    origem = models.CharField(max_length=50, verbose_name='Escola/Empresa atual')
    tipo = models.ForeignKey(TipoParticipante)

    def __str__(self):
        return self.nome.encode('utf8')

    class Meta:
        ordering = ["nome"]

class Inscricao(models.Model):

    STATUS_CHOICES = ((1, u'Aguardando pagamento'),
                       (2, u'Em analise'),
                       (3, u'Paga'),
                       (4, u'Disponivel'),
                       (5, u'Em disputa'),
                       (6, u'Devolvida'),
                       (7, u'Cancelada'))

    data = models.DateTimeField(auto_now=True)
    participante = models.ForeignKey('Participante') #exemplo para nao exigir a existencia da classe ao compilar
    atividades = models.ManyToManyField(Atividade)
    estado = models.IntegerField(editable=False, choices=STATUS_CHOICES, default=1)

    def __str__(self):
        return str(self.id).encode('utf8')

    class Meta:
        ordering = ["data"]