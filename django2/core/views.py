from django.shortcuts import render
from .forms import ContatoForm, ProdutoModelForm
from django.contrib import messages
from .models import Produto
from django.shortcuts import redirect

def index(request):
    context = {
        'produtos': Produto.objects.all()
    }
    return render(request, 'index.html', context)

def contato(request):
    form = ContatoForm(request.POST or None)

    if str(request.method) == 'POST':
        if form.is_valid():

            form.send_mail()

            # nome = form.cleaned_data['nome']
            # email = form.cleaned_data['email']
            # assunto = form.cleaned_data['assunto']
            # mensagem = form.cleaned_data['mensagem']

            # print(f'Nome: {nome}')
            # print(f'Email: {email}')
            # print(f'Email: {assunto}')
            # print(f'Mensagem: {mensagem}')

            messages.success(request, 'Email enviado com successo!')
            form = ContatoForm()
        else:
            messages.error(request, 'Erro ao enviar email')


    context = {
        'form': form
    }

    return render(request, 'contato.html', context)

def produto(request):
    if str(request.user) != 'AnonymousUser':
        if str(request.method) == 'POST':
            form = ProdutoModelForm(request.POST, request.FILES)
            if form.is_valid():
            
                form.save()

                messages.success(request, 'Produto salvo com sucesso')
                form = ProdutoModelForm()
            else:
                messages.error(request, 'Erro ao salvar produto')
        else:
            form = ProdutoModelForm()
        
        context = {
            'form': form
        }
        return render(request, 'produto.html', context)
    else:
        return redirect('index')