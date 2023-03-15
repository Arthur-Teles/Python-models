from django.db import models

# Create your models here.

class Estilo(models.Model):
    nome = models.CharField(max_length = 30)
    anos_de_existencia = models.IntegerField()
    popular_no_brasil = models.BooleanField()
    instrumento_mais_usado = models.CharField(max_length = 30)

    def __str__(self):
        return self.nome

class Musico(models.Model):
    nome = models.CharField(max_length = 50)
    idade = models.IntegerField()
    email_contato = models.EmailField()
    pais_origem = models.CharField(max_length = 30)
    genero = models.CharField(max_length=10)

class Banda(models.Model):
    nome = models.CharField(max_length = 30)
    data_criacao = models.DateField(auto_now = False, auto_now_add = False)
    num_albuns = models.IntegerField()
    faz_musicas_ainda = models.BooleanField()
    estilo_musical = models.ForeignKey(Estilo, on_delete = models.CASCADE)
    musicos = models.ManyToManyField(Musico)

    def __str__(self):
        return self.nome



