from django.urls import path
from erp.views import HomeView, cria_funcionario, lista_funcionario, busca_funcionario_por_id, atualiza_funcionario, \
    ProdutoCreateView

app_name = 'erp'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('funcionarios/', lista_funcionario, name='lista_funcionario'),
    path('funcionarios/novo', cria_funcionario, name='cria_funcionario'),
    path('funcionarios/detalhe/<pk>', busca_funcionario_por_id, name='busca_funcionario_por_id'),
    path('funcionarios/atualiza/<pk>', atualiza_funcionario, name='atualiza_funcionario'),

    path('produtos/novo', ProdutoCreateView.as_view(), name='cria_produto')
]


