from django.shortcuts import render
from django.http import HttpResponse
from posts.models import *
from .forms import *

def index(request):
	dpto = Departamento.objects.filter(codigoDepartamento = "0800")[0]
	return render(request, 'index.html', {'dpto': dpto.nombreDepartamento})

def materia(request):
    # return HttpResponse("<h1>Asco</h1>")
    if request.method == 'POST':
        form = RegistrarMatForm(request.POST)
        if form.is_valid():
            # a = Asignatura.objects.all().first().codigoMateria

            asignatura = Asignatura(
                        codigoMateria     = form.cleaned_data[ 'codigoMateria' ].upper(),
                        nombreMateria     = form.cleaned_data['nombreMateria'],
                        unidadesCredito   = form.cleaned_data['unidadesCredito'],
                        area              = form.cleaned_data['area'],
                        programaPertenece = form.cleaned_data['programaPertenece'],
                        departamento      = form.cleaned_data['departamento'])
            asignatura.save()

            return HttpResponse('Guardado')
        else:
            return render(request, 'postgrado/materia.html', {'form':form})
    else:
        form = RegistrarMatForm()
        return render(request, 'postgrado/materia.html', {'form':form})
