from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Produto
from django.http import HttpResponse
from django.template import loader

def index(request):
    # print(dir(request))
    # print(f"user = {request.user}")

    produtos = Produto.objects.all()

    if str(request.user) == 'AnonymousUser':
        teste ='Usuário não logado'
        nome = ''
    else:
        nome = request.user
        teste = 'Usuário logado'


    context = {
        'curso': 'Curso',
        'logado': teste,
        'nome': nome,
        'produtos': produtos
    }
    return render(request, 'index.html', context)

def contato(request):
    return render(request, 'contato.html')


def produto(request, pk):
    #prod = Produto.objects.get(id=pk)
    
    prod = get_object_or_404(Produto, id=pk)

    context = {
        'produto' : prod
    }
    return render(request, 'produto.html', context)

def error404(request, exception):
    template = loader.get_template('404.html')
    return HttpResponse(content= template.tender(), content_type = 'text/html; charset=utf8', status =404)

def error500(request, exception):
    template = loader.get_template('500.html')
    return HttpResponse(content= template.tender(), content_type = 'text/html; charset=utf8', status =500)