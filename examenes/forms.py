from django import forms
from .models import Examen

class ExamenForm(forms.ModelForm):
    class Meta:
        model = Examen
        fields = [
            'paciente',
            'descripcion',
            #'dateTime',
        ]

        labels = {
            'paciente' : 'Paciente',
            'descripcion' : 'Descripcion',
            #'dateTime' : 'Date Time',
        }
