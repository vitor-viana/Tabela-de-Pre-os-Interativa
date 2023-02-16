from django.shortcuts import render, HttpResponse
from core.models import Sessao, Produto

# Create your views here.

class SessaoProdutos:
    def __init__(self, nome_sessao, produtos):
        self.nome_sessao = nome_sessao
        self.produtos = produtos

def index (request):
    sessoes = Sessao.objects.all ()

    lista_sessoes = []
    for sessao in sessoes:
        nova_sessao_produtos = SessaoProdutos (sessao, Produto.objects.filter (sessao=sessao))
        lista_sessoes.append(nova_sessao_produtos)
    
    dados = {'lista_sessoes':lista_sessoes, 'sessoes':sessoes}
    
    return render (request, 'index.html', dados)
