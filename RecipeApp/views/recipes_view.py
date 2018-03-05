from django.shortcuts import render
from RecipeApp.models import Recipe, Ingredient

def recipes(request):
	id = request.GET.get('id')
	if id is not None:
		recipe = Recipe.objects.filter(id = id)[0]
		lines = recipe.recipe_text.split('\n')
		ingredients = Ingredient.objects.filter(recipe = recipe)
		return render(request, 'RecipeApp/recipe.html', {'recipe' : recipe, 'lines' : lines, 'ingredients' : ingredients})
	else:
		recipes = Recipe.objects.all()
		list_recipes = [entry for entry in recipes]
		
		if len(list_recipes) == 0:
			return render(request, 'RecipeApp/recipes.html', {'message' : 'No recipes are available.'})
		else:
		
			return render(request, 'RecipeApp/recipes.html', {'recipes' : list_recipes})