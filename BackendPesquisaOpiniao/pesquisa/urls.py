from django.urls import path
from .views import *

urlpatterns = [
    path("permissao/", PermissaoAPIView.as_view(), name='permissao'),
    path('permissao/<int:pk>/', PermissaoAPIView.as_view(), name='permissaoParameters'),

    path("tiposperguntas/", TipoPerguntaAPIView.as_view(), name='tiposperguntas'),
    path('tiposperguntas/<int:pk>/', TipoPerguntaAPIView.as_view(), name='tiposPerguntasParameters'),

    path("resposta/", RespostaAPIView.as_view(), name='resposta'),
    path('resposta/<int:pk>/', RespostaAPIView.as_view(), name='respostaParameters'),

    path("usuario/", UsuarioAPIView.as_view(), name='usuario'),
    path('usuario/<int:pk>/', UsuarioAPIView.as_view(), name='usuarioParameters'),

    path("pesquisa/", PesquisaAPIView.as_view(), name='pesquisa'),
    path('pesquisa/<int:pk>/', PesquisaAPIView.as_view(), name='pesquisaParameters'),

    path("formulario/", FormularioAPIView.as_view(), name='formulario'),
    path('formulario/<int:pk>/', FormularioAPIView.as_view(), name='formularioParameters'),

]