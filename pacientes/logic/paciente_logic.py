from ..models import Paciente

def get_pacientes():
    queryset = Paciente.objects.all()
    return (queryset)

def create_paciente(form):
    examen = form.save()
    examen.save()
    return ()