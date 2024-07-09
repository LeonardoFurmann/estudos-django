from django.shortcuts import render
from .forms import ContatoForm
from django.contrib import messages

def index(request):
    return render(request, 'index.html')

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
    return render(request, 'produto.html')