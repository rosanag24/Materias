from django.shortcuts import render
from django.http import HttpResponse
from posts.models import *

def index(request):
	dpto = Departamento.objects.filter(codigoDepartamento = "0800")[0]
	return render(request, 'index.html', {'dpto': dpto.nombreDepartamento})