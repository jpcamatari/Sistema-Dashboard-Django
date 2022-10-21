from django.shortcuts import render
from .models import Movimento
from django.http import JsonResponse
from django.db.models import Sum

def home(request):
    return render(request, 'home.html')

def total_gasto(request):
    total = Movimento.objects.all().aaggregate(Sum('valor'))['valor__sum']
    return JsonResponse({'Valor': total})