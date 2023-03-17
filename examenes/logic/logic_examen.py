from ..models import Examen

def get_examenes():
    queryset = Examen.objects.all().order_by('-dateTime')[:10]
    return (queryset)

def create_examen(form):
    examen = form.save()
    examen.save()
    return ()