from django.db import models

class Permissao(models.Model):
    nomePermissao = models.CharField(max_length=55)
    def __str__(self):
        return self.nomePermissao 

class TipoPergunta(models.Model):
    nomeTipoPergunta = models.CharField(max_length=55)
    def __str__(self):
        return self.nomeTipoPergunta 

class Resposta(models.Model):
    resposta = models.CharField(default=" ", max_length=300)
    def __str__(self):
        return self.resposta 

class Usuario(models.Model):
    nomeUsuario = models.CharField(max_length=50)
    senhaUsuario = models.CharField(max_length=20)
    edvUsuario = models.CharField(max_length=15)
    admUsuario = models.BooleanField()
    fkPermissao = models.ForeignKey(Permissao, related_name=("nomePesquisa+"), on_delete=models.CASCADE)
    def __str__(self):
        return self.nomeUsuario 

class Pesquisa(models.Model):
    nomePesquisa = models.CharField(max_length=50)
    criador = models.CharField(max_length=50)
    anonimo = models.BooleanField()
    fkPermissao  = models.ForeignKey(Permissao, related_name=("nomePermissao+"), on_delete=models.CASCADE)
    def __str__(self):
        return self.nomePesquisa

class Formulario(models.Model):
    enunciado = models.CharField(max_length=150)
    fkResposta = models.ForeignKey(Resposta, related_name=("resposta+"), on_delete=models.CASCADE)
    fkPesquisa = models.ForeignKey(Pesquisa, related_name=("nomePesquisa+"), on_delete=models.CASCADE)
    fkTipoPergunta = models.ForeignKey(TipoPergunta, related_name=("nomeTipoPergunta+"), on_delete=models.CASCADE)
    def __str__(self):
        return self.enunciado 











