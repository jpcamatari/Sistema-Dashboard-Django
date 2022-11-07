from django.shortcuts import render
from .models import Movimento
from django.http import JsonResponse, HttpResponse
from .forms import formularioLancar

def home(request):
    return render(request, 'home.html')


def lancar(request):
   form = formularioLancar()
   return render(request, 'lancar.html', {'form': form})

def processa_formulario(request):
    return HttpResponse('teste')