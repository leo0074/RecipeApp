from django.shortcuts import render
from RecipeApp.models import Recipe, Ingredient

def recipes(request):
	recipes = Recipe.objects.values()
	list_recipes = [entry for entry in recipes]
	return render(request, 'RecipeApp/recipes.html', {'recipes' : list_recipes})