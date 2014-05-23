from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, authenticate

from django.contrib.auth import login, authenticate, logout

from django.contrib.auth.decorators import login_required, permission_required

#@login_required(login_url='/usuario/login/')
@permission_required('auth.add_user', login_url='/usuario/login/')
def nuevo_usuario(request):
	if request.method == 'POST':
		formulario = UserCreationForm(request.POST)
		if formulario.is_valid():
			formulario.save()
			return HttpResponseRedirect('/index/')
	else:
		formulario = UserCreationForm()
		return render_to_response('usuarios/new_user.html', {'formulario':formulario}, context_instance=RequestContext(request))

def iniciar_sesion(request):
	if not request.user.is_anonymous():
		return HttpResponseRedirect('/index/')
	if request.method == 'POST':
		formulario = AuthenticationForm(request.POST)
		if formulario.is_valid:
			username = request.POST['username']
			clave = request.POST['password']
			acceso = authenticate(username = username, password = clave)
			if acceso is not None:
				if acceso.is_active:
					login(request, acceso)
					return HttpResponseRedirect('/index/')
				else:
					return HttpResponseRedirect('/index/')
			else:
				return HttpResponseRedirect('/index/')
	else:
		formulario = AuthenticationForm()

	return render_to_response('usuarios/login.html', {'formulario':formulario}, context_instance=RequestContext(request))

@login_required(login_url = '/usuario/login/')
def cerrar_sesion(request):
	logout(request)
	return HttpResponseRedirect('/index/')