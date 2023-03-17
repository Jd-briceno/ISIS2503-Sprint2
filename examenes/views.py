from django.shortcuts import render
from .forms import ExamenForm
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from .logic.logic_examen import create_examen, get_examenes

def examen_list(request):
    examenes = get_examenes()
    context = {
        'examen_list': examenes
    }
    return render(request, 'Examen/examenes.html', context)

def examen_create(request):
    if request.method == 'POST':
        form = ExamenForm(request.POST)
        if form.is_valid():
            create_examen(form)
            messages.add_message(request, messages.SUCCESS, 'Examen creado con exito')
            return HttpResponseRedirect(reverse('examenCreate'))
        else:
            print(form.errors)
    else:
        form = ExamenForm()

    context = {
        'form': form,
    }

    return render(request, 'Examen/examenCreate.html', context)