from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    sexo = 'M'
    nome = 'Alfredo'
    lista = [
        {'nome': 'João', 'sexo': 'M'},
        {'nome': 'José', 'sexo': 'm'},
        {'nome': 'Maria', 'sexo': 'F'},
        {'nome': 'Joaquina', 'sexo': 'f'},
    ]

    informacoes = {'lista': lista, 'sexo': sexo, 'nome': nome}
    return render(request, 'index.html', informacoes)