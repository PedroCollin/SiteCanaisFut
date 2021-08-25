from django.shortcuts import render
from django.contrib import messages
from django.core.validators import validate_email

def login(request):
    return render(request,'usuarios/login.html')

def logout(request):
    return render(request, 'usuarios/logout.html')

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

def dashboard(request):
    return render(request,'usuarios/dashboard.html')

