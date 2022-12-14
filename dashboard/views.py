from django.shortcuts import render
from .forms import formularioLancar
from .models import Movimento
from django.http import JsonResponse, HttpResponse
from django.db.models import Sum
from datetime import datetime

#Tras todos os elementos do banco de dados utilizando ORM do django e renderiza a pagina
def home(request):
    lista = Movimento.objects.all()
    context = {
        'lista' : lista,
    }
    return render(request, 'home.html', context)

#Renderiza a pagina e tras formulario em django para inserção no banco de dados
def lancar(request):
    form = formularioLancar(request.POST)
    if form.is_valid():
        form.save()
        return render(request, 'lancar.html', {'form': form})
    return render(request, 'lancar.html', {'form': form})
 
#Função do ORM que busca todas as linhas do banco e soma a coluna valor
def total_gasto(request):
    total = Movimento.objects.all().aggregate(Sum('valor'))['valor__sum']
    return JsonResponse({'total' : total})

#Função que captura o mes atual, gera os gastos dos ultimos 12 meses e envia um resposta http
def relatorio_gasto(request):
    x = Movimento.objects.all()

    meses = ['jan', 'fev', 'mar', 'abr', 'mai', 'jun', 'jul', 'ago', 'set', 'out', 'nov', 'dez']
    data = []
    labels = []
    cont = 0
    mes = datetime.now().month + 1
    ano = datetime.now().year
    for i in range(12):
        mes -= 1
        if mes == 0:
            mes = 12
            ano -= 1
        
        y = sum([i.valor for i in x if i.data.month == mes and i.data.year == ano])
        labels.append(meses[mes-1])
        data.append(y)
        cont += 1

    data_json = {'data' : data[::-1], 'labels' : labels[::-1]}
    return JsonResponse(data_json)
