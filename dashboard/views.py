from django.shortcuts import render
from .models import Movimento
from django.http import JsonResponse
from django.db.models import Sum

def home(request):
    return render(request, 'home.html')


def lancar(request):
    if request.method == "GET":
        return render(request, 'lancar.html')
    else:
        data = request.POST.get("data")
        descricao = request.POST.get("descrição")
        categoria = request.POST.get("categoria")
        categoria = request.POST.get("valor")


def total_gasto(request):
    total = Movimento.objects.all().aaggregate(Sum('valor'))['valor__sum']
    return JsonResponse({'Valor': total})