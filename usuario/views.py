from django.shortcuts import render


def login(request):
    return render(request,'usuarios/login.html')

def logout(request):
    return render(request, 'usuarios/logout.html')

def cadastrar(request):
    return render(request,'usuarios/cadastrar.html')

def dashboard(request):
    return render(request,'usuarios/dashboard.html')

