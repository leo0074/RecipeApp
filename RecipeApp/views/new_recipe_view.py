from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required


@login_required
def new_recipe(request):

	if request.method == 'POST':
		username = request.user.username
		ingredients = []
		recipe = request.POST['recipe']
		return render(request, 'RecipeApp/new_recipe.html')
	
	if request.method == 'GET':

		return render(request, 'RecipeApp/new_recipe.html')