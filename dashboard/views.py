from django.shortcuts import render
from .forms import formularioLancar
from .models import Movimento

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
 

