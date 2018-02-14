from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.http import HttpResponse


def login_page(request):

	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			next = request.POST['next']
			if next != '':
				return render(request, next[1:]+'.html')
			else:
				return render(request, 'RecipeApp/login_success.html')
		else:
			return render(request, 'RecipeApp/login.html', {'username' : username, 'message' : 'Invalid username or password', 'next' : request.POST['next']})
	
	if request.method == 'GET':
		if 'next' in request.GET:
			return render(request, 'RecipeApp/login.html', {'next' : request.GET['next'], 'message' : 'This pages requires a login'})
		else:
			return render(request, 'RecipeApp/login.html')
			
	