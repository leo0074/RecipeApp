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
			return HttpResponse('Login successful!')
		else:
			return render(request, 'RecipeApp/login.html', {'username' : username, 'message' : 'Invalid username or password'})
	if request.method == 'GET':
		return render(request, 'RecipeApp/login.html')
	