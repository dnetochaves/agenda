from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.core.validators import validate_email
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import FormContato

# Create your views here.


def index_login(request):
    pass


def login(request):
    if request.method != 'POST':
        return render(request, 'contas/login.html')

    usuario = request.POST.get('usuario')
    senha = request.POST.get('senha')
    user = auth.authenticate(request, username=usuario, password=senha)

    if not user:
        messages.error(request, 'Usuário ou senha inválidos.')
        return render(request, 'accounts/login.html')
    else:
        auth.login(request, user)
        messages.success(request, 'Você fez login com sucesso.')
        return redirect('dashboard')


def logout(request):
    auth.logout(request)
    return redirect('index')


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


@login_required(login_url='/contas/login/')
def dashboard(request):
    if request.method != 'POST':
        form = FormContato()
        return render(request, 'contas/dashboard.html', {'form': form })
    form = FormContato(request.POST, request.FILES)
    
    if not form.is_valid():
        messages.add_message(request, messages.ERROR, 'Erro ao enviar formulário')
        form = FormContato(request.POST)
        return render(request, 'contas/dashboard.html', {'form': form })
    
    form.save()
    messages.add_message(request, messages.SUCCESS, f'Contato {request.POST.get("nome")} salvo com sucesso')
    return redirect('dashboard')
        
