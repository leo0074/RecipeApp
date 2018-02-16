from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required


@login_required
def new_recipe(request):

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

		return render(request, 'RecipeApp/new_recipe.html')