from django import forms
from .models import Examen

class ExamenForm(forms.ModelForm):
    class Meta:
        model = Examen
        fields = [
            'paciente',
            'value',
            'unit',
            'place',
            #'dateTime',
        ]

        labels = {
            'paciente' : 'Paciente',
            'value' : 'Value',
            'unit' : 'Unit',
            'place' : 'Place',
            #'dateTime' : 'Date Time',
        }
