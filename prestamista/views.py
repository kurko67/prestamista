from django.shortcuts import render
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib import messages
from django.contrib.auth import authenticate
from django.shortcuts import redirect
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required


def index(request):
	return render(request,'frontEnd/index.html',{

	})

@login_required(login_url='login')
def my(request):
	return render(request, 'backend/index.html',{

	})

def login_view(request):
	if request.user.is_authenticated:
		return redirect('index')

	if request.method == 'POST':
		username = request.POST.get('username') #es un diccionario por eso usa get
		password = request.POST.get('password')
		user = authenticate(username=username, password=password)
		if user:
			login(request, user)
			messages.success(request,'Bienvenido {}'.format(user.username))

			if request.GET.get('next'):
				return HttpResponseRedirect(request.GET['next'])
			else:
				return redirect('my')
		else:
			messages.error(request,'Datos incorrectos, por favor verifique')

	return render(request, 'users/login.html',{

		})

def logout_view(request):
	logout(request)
	messages.success(request,'Session cerrada exitosamente')
	return redirect('login')
