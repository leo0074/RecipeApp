from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import HttpResponse


def login(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		if user is not None:
			#login(request, user)
			return HttpResponse("Login successful!")
		else:
			return HttpResponse("Login failed")
	if request.method == 'GET':
		return render(request, 'RecipeApp/login.html')
	