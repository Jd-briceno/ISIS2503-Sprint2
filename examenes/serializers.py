from rest_framework import serializers
from . import models


class ExamenSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'paciente', 'descripcion', 'time',)
        model = models.Examen