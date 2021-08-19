from django.shortcuts import render, Http404, get_object_or_404, redirect
from .models import TeamMates
from django.db.models import Q
from django.contrib import messages

# Create your views here.

def index(request):
    dados = TeamMates.objects.order_by('id').filter(
        mostrar=True
    )

    return render(request,'home/index.html',{'dados':dados})

def mostrar(request,idbusca):
    dados = get_object_or_404(TeamMates, id=idbusca)
    return render(request,'home/times.html',{'dados':dados})

def buscar(request):
    x = request.GET['buscar']

    if x is None or not x:
        messages.add_message(request,messages.INFO,'Digite um valor valido')
        redirect('home')

    dados = TeamMates.objects.order_by('nometeam').filter(
        Q(nometeam__icontains=x)

    )
    return render(request,'home/index.html',{'dados':dados})