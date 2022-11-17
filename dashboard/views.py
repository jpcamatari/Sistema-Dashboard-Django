from django.shortcuts import render
from .forms import formularioLancar
from .models import Movimento

def home(request):
    lista = Movimento.objects.all()
    total = Movimento.objects.annotate(somatoria=Sum('valor'))
    context = {
        'lista' : lista,
        'total' : total
    }
    return render(request, 'home.html', context)


def lancar(request):
    form = formularioLancar(request.POST)
    if form.is_valid():
        form.save()
        return render(request, 'lancar.html', {'form': form})
    return render(request, 'lancar.html', {'form': form})
 

