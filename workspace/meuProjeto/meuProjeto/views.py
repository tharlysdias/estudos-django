from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    minha_variavel = 'Programe Facil'
    return render(request, 'index.html', {'minha_variavel': minha_variavel})