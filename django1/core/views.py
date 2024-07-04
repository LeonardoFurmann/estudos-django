from django.shortcuts import render

def index(request):
    # print(dir(request))
    # print(f"user = {request.user}")

    if str(request.user) == 'AnonymousUser':
        teste ='Usuário não logado'
        nome = ''
    else:
        nome = request.user
        teste = 'Usuário logado'


    context = {
        'curso': 'Curso',
        'logado': teste,
        'nome': nome
    }
    return render(request, 'index.html', context)

def contato(request):
    return render(request, 'contato.html')