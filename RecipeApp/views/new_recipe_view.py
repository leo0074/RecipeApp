from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from RecipeApp.models import Recipe, Ingredient
from django.utils import timezone
@login_required
def new_recipe(request):

	if request.method == 'POST':
		recipeName = request.POST['name']
		recipeText = request.POST['recipe']
		ingredientAmount = int(request.POST['amount'])
		recipe = Recipe(owner=request.user, recipe_text = recipeText, created_date = timezone.now())
		print(recipe.recipe_text)
		recipe.save()
		for x in range(ingredientAmount, 0, -1):
			if request.POST['ingredient'+str(x)] != "":
				ingredient = Ingredient(recipe = recipe, name = request.POST['ingredient'+str(x)], unit = request.POST['unit'+str(x)])
				print(ingredient.name)
				print(ingredient.unit)
				ingredient.save()
		
		return render(request, 'RecipeApp/new_recipe.html', {'message' : 'Recipe posted successfully'})
	
	if request.method == 'GET':

		return render(request, 'RecipeApp/new_recipe.html')