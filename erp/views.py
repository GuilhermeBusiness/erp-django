from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpRequest, HttpResponseRedirect, Http404
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, ListView, UpdateView, DetailView, DeleteView
from erp.forms import FuncionarioForm, ProdutoForm, VendaForm
from erp.models import Funcionario, Produto, Venda


class ErpLoginView(LoginView):
    template_name = 'erp/login.html'
    success_url = reverse_lazy('erp:dashboard')
    redirect_authenticated_user = True

class ErpLogoutView(LogoutView):
    template_name = 'erp/logout.html'

class HomeView(TemplateView):
    template_name = 'erp/index.html'


class DashboardView(TemplateView):
    template_name = 'erp/dashboard.html'

def cria_funcionario(req: HttpRequest):
    if req.method == 'GET':
        form = FuncionarioForm()

        return render(
            req,
            template_name='erp/funcionarios/novo.html',
            context={'form': form}
        )

    elif req.method == 'POST':
        form = FuncionarioForm(req.POST)

        if form.is_valid():
            funcionario = Funcionario(**form.cleaned_data)

            funcionario.save()

            return HttpResponseRedirect(redirect_to='/')


def lista_funcionarios(req: HttpRequest):
    if req.method == 'GET':
        funcionarios = Funcionario.objects.all()

        return render(
            req,
            template_name='erp/funcionarios/lista.html',
            context={'funcionarios': funcionarios}
        )


def busca_funcionario_por_id(req: HttpRequest, pk: int):
    if req.method == 'GET':

        try:
            funcionario = Funcionario.objects.get(pk=pk)
        except Funcionario.DoesNotExist:
            funcionario = None

        return render(
            req,
            template_name='erp/funcionarios/detalhe.html',
            context={'funcionario': funcionario}
        )


def atualiza_funcionario(req: HttpRequest, pk: int):
    if req.method == 'GET':
        funcionario = Funcionario.objects.get(pk=pk)
        form = FuncionarioForm(instance=funcionario)

        return render(
            req,
            template_name='erp/funcionarios/atualiza.html',
            context={'form': form}
        )


    elif req.method == 'POST':
        funcionario = Funcionario.objects.get(pk=pk)
        form = FuncionarioForm(req.POST, instance=funcionario)

        if form.is_valid():
            form.save()

            return HttpResponseRedirect(redirect_to=f'/funcionarios/detalhe/{pk}')


# Produtos

class ProdutoCreateView(CreateView):
    template_name = 'erp/produtos/novo.html'
    model = Produto
    form_class = ProdutoForm
    success_url = reverse_lazy('erp:home')


class ProdutoListView(ListView):
    model = Produto
    template_name = 'erp/produtos/lista.html'
    context_object_name = 'produtos'


class ProdutoUpdateView(UpdateView):
    model = Produto
    template_name = 'erp/produtos/atualiza.html'
    form_class = ProdutoForm
    success_url = reverse_lazy('erp:lista_produtos')


class ProdutoDetailView(DetailView):
    model = Produto
    template_name = 'erp/produtos/detalhe.html'
    context_object_name = 'produto'

    def get_object(self, queryset=None):
        try:
            return super().get_object(queryset)
        except Http404:
            return None


class ProdutoDeleteView(DeleteView):
    model = Produto
    template_name = 'erp/produtos/deleta.html'
    context_object_name = 'produto'
    success_url = reverse_lazy('erp:lista_produtos')

    def get_object(self, queryset=None):
        try:
            return super().get_object(queryset)
        except Http404:
            return None

class VendaListView(ListView):
    model = Venda
    template_name = 'erp/vendas/lista.html'
    context_object_name = 'vendas'


class VendaCreateView(CreateView):
    model = Venda
    template_name = "erp/vendas/novo.html"
    success_url = reverse_lazy('erp:home')
    fields = ['funcionario', 'produto']

class VendaDetailView(DetailView):
    model = Venda
    template_name = 'erp/vendas/detalhe.html'
    context_object_name = 'venda'

    def get_object(self, queryset=None):
        try:
            return super().get_object(queryset)
        except Http404:
            return None

class VendaUpdateView(UpdateView):
    model = Venda
    template_name = 'erp/vendas/atualiza.html'
    form_class = VendaForm
    success_url = reverse_lazy('erp:lista_vendas')

class VendaDeleteView(DeleteView):
    model = Venda
    template_name = 'erp/vendas/deleta.html'
    context_object_name = 'venda'
    success_url = reverse_lazy('erp:lista_vendas')

    def get_object(self, queryset=None):
        try:
            return super().get_object(queryset)
        except Http404:
            return None


