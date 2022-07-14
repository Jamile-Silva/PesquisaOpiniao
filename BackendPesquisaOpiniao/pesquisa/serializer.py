from rest_framework import serializers
from .models import *


class RespostaSerializer(serializers.ModelSerializer):
    class Meta:
        many = True
        model = Resposta
        fields = '__all__'

class PermissaoSerializer(serializers.ModelSerializer):
    class Meta:
        many = True
        model = Permissao
        fields = '__all__'

class TipoPerguntaSerializer(serializers.ModelSerializer):
    class Meta:
        many = True
        model = TipoPergunta
        fields = '__all__'

class UsuarioGETSerializer(serializers.ModelSerializer):
    fkPermissao = PermissaoSerializer(read_only=True)
    class Meta:
        many = True
        model = Usuario
        fields = '__all__'

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        many = True
        model = Usuario
        fields = '__all__'

class PesquisaGETSerializer(serializers.ModelSerializer):
    fkPermissao = PermissaoSerializer(read_only=True)
    class Meta:
        many = True
        model = Pesquisa
        fields = '__all__'
    
class PesquisaSerializer(serializers.ModelSerializer):
    class Meta:
        many = True
        model = Pesquisa
        fields = '__all__'

class FormularioGETSerializer(serializers.ModelSerializer):
    fkResposta =RespostaSerializer(read_only=True)
    fkPesquisa = PesquisaSerializer(read_only=True)
    fkTipoPergunta = TipoPerguntaSerializer(read_only=True)
    class Meta:
        many = True
        model = Formulario
        fields = '__all__'

class FormularioSerializer(serializers.ModelSerializer):
    class Meta:
        many = True
        model = Formulario
        fields = '__all__'

