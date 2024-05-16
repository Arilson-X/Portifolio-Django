from django.db import models
from datetime import datetime

class Projeto(models.Model):
    OPCOES_CATEGORIA = [
        ("AD" , "Analise de dados"),
        ("CD" , "Ciencia de dados"),
        ("AM" , "Aprendizado de Maquina"),
        ("D" , "Desenvolvimento"),
    ]
    nome = models.CharField(max_length=50, null=False, blank=False)
    tipo = models.CharField(max_length=100, choices=OPCOES_CATEGORIA, default='')
    descricao = models.TextField(null=False, blank=False)
    data = models.DateTimeField(default=datetime.now,blank=False)
    tecnologias = models.CharField(max_length=100,default='')
    imagem = models.ImageField(upload_to="imagem/%Y/%m/%d/", blank=True)
    imagem_capa = models.ImageField(upload_to="imagem/capa/%Y/%m/%d/", blank=True)


    def __str__(self):
        return self.nome
    
class Curso(models.Model):
    OPCOES_CATEGORIA = [
        ("AD" , "Analise de dados"),
        ("CD" , "Ciencia de dados"),
        ("AM" , "Aprendizado de Maquina"),
        ("D" , "Desenvolvimento"),
        ("DP", "Desenvolvimento Pessoal"),
    ]
    nome = models.CharField(max_length=50, null=False, blank=False)
    plataforma = models.CharField(max_length=50, null=False, blank=False)
    tipo = models.CharField(max_length=100, choices=OPCOES_CATEGORIA, default='')
    descricao = models.TextField(null=False, blank=False)
    data = models.DateTimeField(default=datetime.now,blank=False)
    tecnologias = models.CharField(max_length=100,default='')
    imagem = models.ImageField(upload_to="imagem/%Y/%m/%d/", blank=True)
    imagem_capa = models.ImageField(upload_to="imagem/capa/%Y/%m/%d/", blank=True)
    concluido = models.BooleanField(default=True)


    def __str__(self):
        return self.nome

class Experiencia(models.Model):
    empresa = models.CharField(max_length=50, null=False, blank=False)
    descricao = models.TextField(null=False, blank=False)
    data_inicio = models.DateTimeField(default=datetime.now,blank=False)
    data_fim = models.DateTimeField()
    tecnologias = models.CharField(max_length=100,default='')

    def __str__(self):
        return self.empresa