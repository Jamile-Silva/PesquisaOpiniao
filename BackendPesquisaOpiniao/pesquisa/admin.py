from django.contrib import admin
from .models import *

class detPermissao(admin.ModelAdmin):
    list_display = ('id','nomePermissao')
    list_display_links = ('id',)
    search_fields = ('nomePermissao',)
    list_per_page = 10

admin.site.register(Permissao, detPermissao)

class detResposta(admin.ModelAdmin):
    list_display = ('id','resposta')
    list_display_links = ('id',)
    search_fields = ('resposta',)
    list_per_page = 10

admin.site.register(Resposta, detResposta)

class detTipoPergunta(admin.ModelAdmin):
    list_display = ('id','nomeTipoPergunta')
    list_display_links = ('id',)
    search_fields = ('nomeTipoPergunta',)
    list_per_page = 10

admin.site.register(TipoPergunta, detTipoPergunta)

class detUsuario(admin.ModelAdmin):
    list_display = ('id','nomeUsuario', 'senhaUsuario', 'edvUsuario', 'admUsuario', 'fkPermissao')
    list_display_links = ('id',)
    search_fields = ('nomeUsuario',)
    list_per_page = 10

admin.site.register(Usuario, detUsuario)

class detFormulario(admin.ModelAdmin):
    list_display = ('id','enunciado', 'fkResposta', 'fkPesquisa', 'fkTipoPergunta')
    list_display_links = ('id',)
    search_fields = ('enunciado',)
    list_per_page = 10

admin.site.register(Formulario, detFormulario)

class detPesquisa(admin.ModelAdmin):
    list_display = ('id','nomePesquisa', 'criador', 'anonimo', 'fkPermissao', )
    list_display_links = ('id',)
    search_fields = ('nomePesquisa',)
    list_per_page = 10

admin.site.register(Pesquisa, detPesquisa)
