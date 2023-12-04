from django.urls import path
from erp.views import home, cria_funcionario, lista_funcionario, busca_funcionario_por_id, atualiza_funcionario

app_name = 'erp'

urlpatterns = {
    path('', home),
    path('funcionarios/', lista_funcionario),
    path('funcionarios/novo', cria_funcionario),
    path('funcionarios/detalhe/<pk>', busca_funcionario_por_id),
    path('funcionarios/atualiza/<pk>', atualiza_funcionario)
}


