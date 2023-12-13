from django.urls import path
from erp.views import HomeView, cria_funcionario, lista_funcionarios, busca_funcionario_por_id, atualiza_funcionario, \
    ProdutoCreateView, ProdutoListView, ProdutoUpdateView

app_name = 'erp'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('funcionarios/', lista_funcionarios, name='lista_funcionarios'),
    path('funcionarios/novo', cria_funcionario, name='cria_funcionario'),
    path('funcionarios/detalhe/<pk>', busca_funcionario_por_id, name='busca_funcionario_por_id'),
    path('funcionarios/atualiza/<pk>', atualiza_funcionario, name='atualiza_funcionario'),

    path('produtos/', ProdutoListView.as_view(), name='lista_produtos'),
    path('produtos/novo', ProdutoCreateView.as_view(), name='cria_produto'),
    path('produtos/atualiza/<pk>', ProdutoUpdateView.as_view(), name='atualiza_produto')
]


