from django.shortcuts import render
from .forms import HistoriaForm
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from .logic.logic_historia import create_historia, get_historias
import time

def historia_list(request):
    historias = get_historias()
    context = {
        'historia_list': historias
    }
    return render(request, 'Historia/historias.html', context)

def historia_create(request):
    time.sleep(2)
    if request.method == 'POST':
        form = HistoriaForm(request.POST)
        if form.is_valid():
            create_historia(form)
            messages.add_message(request, messages.SUCCESS, 'Historia creada con exito')
            return HttpResponseRedirect(reverse('historiaCreate'))
        else:
            print(form.errors)
    else:
        form = HistoriaForm()

    context = {
        'form': form,
    }

    return render(request, 'Historia/historiaCreate.html', context)

def historia_create_medico(request):
    if request.method == 'POST':
        form = HistoriaForm(request.POST)
        if form.is_valid():
            create_historia(form)
            messages.add_message(request, messages.SUCCESS, 'Historia creada con exito')
            return HttpResponseRedirect(reverse('historiaCreate'))
        else:
            print(form.errors)
    else:
        form = HistoriaForm()

    context = {
        'form': form,
    }

    return render(request, 'Historia/historiaCreate.html', context)
