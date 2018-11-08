from django.shortcuts import render
from django.http import HttpResponse
from posts.models import *

def eliminar(request):
	materias = Asignatura.objects.all()
	dpto = Departamento.objects.filter(codigoDepartamento = "0800")[0]
	if request.method == 'POST':
		item = Asignatura.objects.filter(codigoMateria = request.POST.get('item_id'))       
		item.delete()
		dpto = Departamento.objects.filter(codigoDepartamento = "0800")[0]
		materias = Asignatura.objects.all()
	return render(request, 'index.html', {'materias': materias, 'dpto':dpto})