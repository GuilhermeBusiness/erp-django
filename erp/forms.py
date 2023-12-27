from django import forms
from erp.models import Funcionario, Produto, Venda

'''
class FuncionarioForm(forms.Form):
    nome = forms.CharField(max_length=30, required=True),
    sobrenome = forms.CharField(max_length=70, required=True),
    cpf = forms.CharField(max_length=14, required=True),
    email_fucional = forms.EmailField(max_length=50, required=True),
    remuneracao = forms.DecimalField(max_digits=8, decimal_places=2, required=True)
'''


class FuncionarioForm(forms.ModelForm):
    class Meta:  # Meta é convenção
        model = Funcionario
        fields = [
            'nome',
            'sobrenome',
            'cpf',
            'email_funcional',
            'remuneracao'
        ]


class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = '__all__'
        labels = {
            'descricao': 'Descrição',
            'preco': 'Preço',
            'data-hora' : 'Data/Hora'
        }

class VendaForm(forms.ModelForm):
    class Meta:
        model = Venda
        fields = '__all__'
        labels = {
            'funcionario': 'Funcinário',
            'produto': 'Produto',

        }
