from django.http import HttpResponse


def home(request):
    return HttpResponse('Olá Mundo!')


def clientes(request):
    return HttpResponse('José, Maria e João')