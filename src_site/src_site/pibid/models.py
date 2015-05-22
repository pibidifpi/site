from django.db import models

# Create your models here.

class Empresa(models.Model):
    nome = models.CharField(max_length=50, verbose_name='Nome')
    logo = models.ImageField(upload_to='imagens/', verbose_name='Logo')
    valor = models.FloatField(verbose_name='Valor')
    outros = models.TextField(verbose_name='Outros')

    def __str__(self):
        return self.nome.encode('utf8')

class Evento(models.Model):
    nome = models.CharField(max_length=50, verbose_name='Nome')
    local = models.CharField(max_length=100, verbose_name='Local')
    dataInicio = models.DateField(verbose_name='Data Inicio')
    dataTermino = models.DateField(verbose_name='Data Termino')
    resumo = models.TextField(verbose_name='Resumo')
    empresas = models.ManyToManyField(Empresa)

    def __str__(self):
        return self.nome.encode('utf8')
