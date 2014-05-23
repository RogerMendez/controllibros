from django.shortcuts import render_to_response
from django.template import RequestContext

def home(request):
	return render_to_response('base.html', context_instance = RequestContext(request))

def ejemplo(request):
	titulo = 'Ejemplo'
	nombre = 'Roger'
	lista = [2,3,2,2,4,4,5,5,2,1,1]
	return render_to_response('ejemplo.html', {'titulo' :titulo, 'nombre' :nombre, 'lista' :lista}, context_instance=RequestContext(request))

def form(request):
	return render_to_response('form.html', context_instance = RequestContext(request))


def index(request):
	return render_to_response('base2.html', context_instance=RequestContext(request))
