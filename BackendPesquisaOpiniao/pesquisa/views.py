from django.shortcuts import render
from .models import *
from .serializer import *
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponseRedirect
from rest_framework.permissions import IsAuthenticated

class PermissaoAPIView(APIView):
# permission_classes = (IsAuthenticated,)
    
    def get(self, request, pk=''):
        if 'permissaoNome' in request.GET:
            statusPermissaoNome = request.GET['permissaoNome']
            permissoes = Permissao.objects.filter(nome__contains=statusPermissaoNome)
            serializer = PermissaoSerializer(permissoes, many=True)
            return Response(serializer.data)          
        elif pk == '':
            permissoes = Permissao.objects.all()
            serializer = PermissaoSerializer(permissoes, many=True)
            return Response(serializer.data)
        else:
            permissoes = Permissao.objects.get(id=pk)
            serializer = PermissaoSerializer(permissoes)
            return Response(serializer.data)

    def post(self, request):
        serializer = PermissaoSerializer(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()        
        return Response({"msg": "Inserido com sucesso"})

    def put(self, request, pk=''):
        permissoes = Permissao.objects.get(id=pk)
        serializer = PermissaoSerializer(permissoes, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, pk=''):        
        permissoes = Permissao.objects.get(id=pk)       
        permissoes.delete()
        return Response({"msg": "Apagado com sucesso"})

class TipoPerguntaAPIView(APIView):
# permission_classes = (IsAuthenticated,)  

    def get(self, request, pk=''):
        if 'nomeTipoPergunta' in request.GET:
            statusNome = request.GET['nomeTipoPergunta']
            tiposPerguntas = TipoPergunta.objects.filter(nome__contains=statusNome)
            serializer = TipoPerguntaSerializer(tipoPerguntas, many=True)
            return Response(serializer.data)          
        elif pk == '':
            tipoPerguntas = TipoPergunta.objects.all()
            serializer = TipoPerguntaSerializer(tipoPerguntas, many=True)
            return Response(serializer.data)
        else:
            tipoPerguntas = TipoPergunta.objects.get(id=pk)
            serializer = TipoPerguntaSerializer(tipoPerguntas)
            return Response(serializer.data)

    def post(self, request):
        serializer = TipoPerguntaSerializer(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()        
        return Response({"msg": "Inserido com sucesso"})

    def put(self, request, pk=''):
        tipoPerguntas = TipoPergunta.objects.get(id=pk)
        serializer = TipoPerguntaSerializer(tipoPerguntas, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, pk=''):        
        tipoPerguntas = TipoPergunta.objects.get(id=pk)       
        tipoPerguntas.delete()
        return Response({"msg": "Apagado com sucesso"})

class RespostaAPIView(APIView):
# permission_classes = (IsAuthenticated,)

    def get(self, request, pk=''):
        if 'resposta' in request.GET:
            statusNome = request.GET['resposta']
            respostas = Resposta.objects.filter(nome__contains=statusNome)
            serializer = RespostaSerializer(respostas, many=True)
            return Response(serializer.data)          
        elif pk == '':
            respostas = Resposta.objects.all()
            serializer = RespostaSerializer(respostas, many=True)
            return Response(serializer.data)
        else:
            respostas = Resposta.objects.get(id=pk)
            serializer = RespostaSerializer(respostas)
            return Response(serializer.data)

    def post(self, request):
        serializer = RespostaSerializer(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()        
        return Response({"msg": "Inserido com sucesso"})

    def put(self, request, pk=''):
        respostas = Resposta.objects.get(id=pk)
        serializer = RespostaSerializer(respostas, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, pk=''):        
        respostas = Resposta.objects.get(id=pk)       
        respostas.delete()
        return Response({"msg": "Apagado com sucesso"})

class UsuarioAPIView(APIView):
# permission_classes = (IsAuthenticated,)
    
    def get(self, request, pk=''):
        if 'nomeUsuario' in request.GET:
            statusNome = request.GET['nomeUsuario']
            usuarios = Usuario.objects.filter(nome__contains=statusNome)
            serializer = UsuarioGETSerializer(usuarios, many=True)
            return Response(serializer.data)   
        elif 'Permissao' in request.GET:
            statusUser = request.GET['Permissao']
            usuarios = Usuario.objects.filter(fkPermissao=statusUser)
            serializer = UsuarioGETSerializer(usuarios, many=True)
            return Response(serializer.data)     
        elif pk == '':
            usuarios = Usuario.objects.all()
            serializer = UsuarioGETSerializer(usuarios, many=True)
            return Response(serializer.data)
        else:
            usuarios = Usuario.objects.get(id=pk)
            serializer = UsuarioGETSerializer(usuarios)
            return Response(serializer.data)

    def post(self, request):
        serializer = UsuarioSerializer(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()        
        return Response({"msg": "Inserido com sucesso"})

    def put(self, request, pk=''):
        usuarios = Usuario.objects.get(id=pk)
        serializer = UsuarioSerializer(usuarios, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, pk=''):        
        usuarios = Usuario.objects.get(id=pk)       
        usuarios.delete()
        return Response({"msg": "Apagado com sucesso"})

class PesquisaAPIView(APIView):
# permission_classes = (IsAuthenticated,)
    
    def get(self, request, pk=''):
        if 'nomePesquisa' in request.GET:
            statusNome = request.GET['nomePesquisa']
            pesquisas = Pesquisa.objects.filter(nome__contains=statusNome)
            serializer = PesquisaGETSerializer(pesquisas, many=True)
            return Response(serializer.data)
        elif 'Permissao' in request.GET:
            statusUser = request.GET['Permissao']
            pesquisas = Pesquisa.objects.filter(fkPermissao=statusUser)
            serializer = PesquisaGETSerializer(pesquisas, many=True)
            return Response(serializer.data)     
        elif pk == '':
            pesquisas = Pesquisa.objects.all()
            serializer = PesquisaGETSerializer(pesquisas, many=True)
            return Response(serializer.data)
        else:
            pesquisas = Pesquisa.objects.get(id=pk)
            serializer = PesquisaGETSerializer(pesquisas)
            return Response(serializer.data)

    def post(self, request):
        serializer = PesquisaSerializer(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()        
        return Response({"msg": "Inserido com sucesso"})
        #return Response({"id": serializer.data['id']})

    def put(self, request, pk=''):
        pesquisas = Pesquisa.objects.get(id=pk)
        serializer = PesquisaSerializer(pesquisas, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, pk=''):        
        pesquisas = Pesquisa.objects.get(id=pk)       
        pesquisas.delete()
        return Response({"msg": "Apagado com sucesso"})

class FormularioAPIView(APIView):
# permission_classes = (IsAuthenticated,)

    def get(self, request, pk=''):
        if 'enunciado' in request.GET:
            statusNome = request.GET['enunciado']
            formularios = Formulario.objects.filter(nome__contains=statusNome)
            serializer = FormularioGETSerializer(usuarios, many=True)
            return Response(serializer.data)
        elif 'Resposta' in request.GET:
            statusUser = request.GET['Resposta']
            formularios = Formulario.objects.filter(fkResposta=statusUser)
            serializer = FormularioGETSerializer(usuarios, many=True)
            return Response(serializer.data)   
        elif 'Pesquisa' in request.GET:
            statusUser = request.GET['Pesquisa']
            formularios = Formulario.objects.filter(fkPesquisa=statusUser)
            serializer = FormularioGETSerializer(formularios, many=True)
            return Response(serializer.data)     
        elif 'TipoPergunta' in request.GET:
            statusUser = request.GET['TipoPergunta']
            formularios = Formulario.objects.filter(fkTipoPergunta=statusUser)
            serializer = FormularioGETSerializer(formularios, many=True)
            return Response(serializer.data)    
        elif pk == '':
            formularios = Formulario.objects.all()
            serializer = FormularioGETSerializer(formularios, many=True)
            return Response(serializer.data)
        else:
            formularios = Formulario.objects.get(id=pk)
            serializer = FormularioGETSerializer(formularios)
            return Response(serializer.data)

    def post(self, request):
        serializer = FormularioSerializer(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()        
        return Response({"msg": "Inserido com sucesso"})

    def put(self, request, pk=''):
        formularios = Formulario.objects.get(id=pk)
        serializer = FormularioSerializer(formularios, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, pk=''):        
        formularios = Formulario.objects.get(id=pk)       
        formularios.delete()
        return Response({"msg": "Apagado com sucesso"})

