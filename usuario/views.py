from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.core.validators import validate_email
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

def login(request):

    if request.method != 'POST':
        return render(request, 'usuarios/login.html')

    usuario = request.POST.get('usuario')
    senha1 = request.POST.get('senha1')

    user = auth.authenticate(request,username=usuario,password=senha1)

    if not user:
        messages.add_message(request, messages.ERROR,'Usuário ou senha inválidos')
        return render(request, 'usuarios/login.html')
    else:
        auth.login(request,user)
        return redirect('dashboard')

def logout(request):
    auth.logout(request)
    return redirect('home')

def cadastrar(request):
    if request.method != 'POST':
        return render(request,'usuarios/cadastrar.html')

    # obtendo os dados do form
    email = request.POST.get('email')
    usuario = request.POST.get('usuario')
    nome = request.POST.get('nome')
    sobrenome = request.POST.get('sobrenome')
    senha1 = request.POST.get('senha1')
    senha2 = request.POST.get('senha2')

    if not email or not nome or not usuario or not sobrenome or not senha1 or not senha2:
        messages.add_message(request,messages.WARNING,'Todos os campos são obrigatórios!')
        return render(request, 'usuarios/cadastrar.html')

    try:
        validate_email(email)
    except:
        messages.add_message(request, messages.WARNING, 'email inválido')
        return render(request, 'usuarios/cadastrar.html')

    if len(senha1)<6:
        messages.add_message(request, messages.WARNING, 'Senha deve ter no minimo 6 caracter')
        return render(request, 'usuarios/cadastrar.html')

    if senha1!=senha2:
        messages.add_message(request, messages.WARNING, 'Senhas diferentes')
        return render(request, 'usuarios/cadastrar.html')

    if User.objects.filter(username=usuario).exists():
        messages.add_message(request, messages.WARNING, 'Usuario já existe')
        return render(request, 'usuarios/cadastrar.html')

    if User.objects.filter(email=email).exists():
        messages.add_message(request, messages.WARNING, 'E-mail já existe')
        return render(request, 'usuarios/cadastrar.html')

    user = User.objects.create_user(
        username=usuario,
        email=email,
        first_name=nome,
        last_name=sobrenome,
        password=senha1
    )
    messages.add_message(request,messages.SUCCESS, 'Cadastrado com sucesso!')
    user.save()
    return redirect('login')
@login_required(redirect_field_name='login')
def dashboard(request):
    return render(request,'usuarios/dashboard.html')

