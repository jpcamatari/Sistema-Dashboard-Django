from django.shortcuts import render
from .forms import formularioLancar
from .models import Movimento
from django.http import JsonResponse
from django.db.models import Sum
from datetime import datetime

def home(request):
    lista = Movimento.objects.all()
    context = {
        'lista' : lista,
    }
    return render(request, 'home.html', context)


def lancar(request):
    form = formularioLancar(request.POST)
    if form.is_valid():
        form.save()
        return render(request, 'lancar.html', {'form': form})
    return render(request, 'lancar.html', {'form': form})
 
def total_gasto(request):
    total = Movimento.objects.all().aggregate(Sum('valor'))['valor__sum']
    return JsonResponse({'total' : total})

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

def relatorio_categoria(request):
    categorias = Movimento.objects.all()
    label = []
    data = []
    for categoria in categorias:
        soma_categoria = Movimento.objects.filter(nome_categoria=categoria).aggregate(Sum('valor'))
        

        if not soma_categoria['total__sum']:
            soma_categoria['total__sum'] = 0
        label.append(categoria.nome)
        data.append(soma_categoria['total__sum'])

    x = list(zip(label, data))

    x.sort(key=lambda x: x[1], reverse=True)
    x = list(zip(*x))

    return JsonResponse({'labels': x[0][:3]})