from django.http import HttpRequest, HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import TemplateView

from erp.forms import FuncionarioForm
from erp.models import Funcionario



class HomeView(TemplateView):
    template_name = 'erp/index.html'


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


def lista_funcionario(req: HttpRequest):
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
