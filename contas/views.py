from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.validators import validate_email
from django.contrib.auth.models import User

# Create your views here.


def index_login(request):
    return render(request, 'contas/login.html')


def login(request):
    return render(request, 'contas/login.html')


def logout(request):
    return render(request, 'contas/logout.html')


def cadastro(request):
    if request.method != 'POST':
        messages.add_message(request, messages.INFO, 'Nada postado')
        return render(request, 'contas/cadastro.html')

    nome = request.POST.get('nome')
    sobrenome = request.POST.get('sobrenome')
    email = request.POST.get('email')
    usuario = request.POST.get('usuario')
    senha = request.POST.get('senha')
    senha2 = request.POST.get('senha2')

    if not nome or not sobrenome or not email or not usuario or not senha or not senha2:
        messages.add_message(request, messages.ERROR, 'Preencha os campos')
        return render(request, 'contas/cadastro.html')

    try:
        validate_email(email)
    except:
        messages.add_message(request, messages.ERROR, 'Email inválido')

    if len(senha) < 6:
        messages.add_message(request, messages.ERROR,
                             'Digite uma senha com mais de 6 digitos')
        return render(request, 'contas/cadastro.html')

    if len(usuario) < 3:
        messages.add_message(request, messages.ERROR,
                             'Usuário precisa ter 6 caracteres')
        return render(request, 'contas/cadastro.html')

    if senha != senha2:
        messages.add_message(request, messages.ERROR, 'Senha incorreta')
        return render(request, 'contas/cadastro.html')

    if User.objects.filter(username=usuario).exists():
        messages.add_message(request, messages.ERROR, 'Usuário já existe')
        return render(request, 'contas/cadastro.html')

    if User.objects.filter(email=email).exists():
        messages.add_message(request, messages.ERROR, 'Email já existe')
        return render(request, 'contas/cadastro.html')

    messages.add_message(request, messages.SUCCESS, 'Registrado com sucesso')
    user = User.objects.create_user(
        username=usuario, email=email, password=senha, first_name='nome', last_name='sobrenome')
    user.save()
    return redirect('login')
   

    return render(request, 'contas/cadastro.html')


def dashboard(request):
    return render(request, 'contas/dashboard.html')
