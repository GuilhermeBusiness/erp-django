from django.urls import path
from erp.views import HomeView, cria_funcionario, lista_funcionarios, busca_funcionario_por_id, atualiza_funcionario, \
    ProdutoCreateView, ProdutoListView, ProdutoUpdateView, ProdutoDetailView, ProdutoDeleteView, VendaCreateView, \
    VendaListView, VendaDetailView, VendaUpdateView, VendaDeleteView

app_name = 'erp'


class ProdutoDeletaView:
    pass


urlpatterns = [

    # Funcionários
    path('', HomeView.as_view(), name='home'),
    path('funcionarios/', lista_funcionarios, name='lista_funcionarios'),
    path('funcionarios/novo', cria_funcionario, name='cria_funcionario'),
    path('funcionarios/detalhe/<pk>', busca_funcionario_por_id, name='busca_funcionario_por_id'),
    path('funcionarios/atualiza/<pk>', atualiza_funcionario, name='atualiza_funcionario'),

    # Produtos
    path('produtos/', ProdutoListView.as_view(), name='lista_produtos'),
    path('produtos/novo', ProdutoCreateView.as_view(), name='cria_produto'),
    path('produtos/atualiza/<pk>', ProdutoUpdateView.as_view(), name='atualiza_produto'),
    path('produtos/detalhe/<pk>', ProdutoDetailView.as_view(), name='busca_produto_por_id'),
    path('produtos/deleta/<pk>', ProdutoDeleteView.as_view(), name='deleta_produto'),

    # Vendas
    path('vendas/', VendaListView.as_view(), name='lista_vendas'),
    path('vendas/novo', VendaCreateView.as_view(), name='cria_venda'),
    path('vendas/detalhe/<pk>', VendaDetailView.as_view(), name='detalhes_venda'),
    path('vendas/atualiza/<pk>', VendaUpdateView.as_view(), name='atualiza_venda'),
    path('vendas/deleta/<pk>', VendaDeleteView.as_view(), name='deleta_venda')
]


