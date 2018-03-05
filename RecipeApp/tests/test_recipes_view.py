from django.test import TestCase
from RecipeApp.models import Recipe, Ingredient
from django.test import Client
from django.utils import timezone
from django.contrib.auth.models import User


def init():
	recipes = Recipe.objects.all()
	if len(recipes) == 0:
		recipes.delete()
		

class Recipe_view_tests(TestCase):
	def test_no_recipes(self):
		client = Client()
		response = client.get('/RecipeApp/recipes')
		self.assertContains(response, 'No recipes are available.')
		
	def test_with_2_recipes(self):
		init()
		owner = User.objects.create_user('leo0074', 'leo.palkio@gmail.com' , 'Supaersecretpassword')
		recipe1 = Recipe(owner = owner, name = 'Mudcake', created_date = timezone.now())
		recipe2 = Recipe(owner = owner, name = 'Chocolate cake', created_date = timezone.now())
		recipe1.save()
		recipe2.save()
		client = Client()
		response = client.get('/RecipeApp/recipes')
		self.assertContains(response, 'Mudcake')	
		self.assertContains(response, 'Chocolate cake')	
		
	def test_single_recipe_view(self):
		init()
		owner = User.objects.create_user('leo0074', 'leo.palkio@gmail.com' , 'Supaersecretpassword')
		recipe = Recipe(owner = owner, name = 'Mudcake', created_date = timezone.now(), recipe_text = 'Just throw everything to oven and see what happens!')
		recipe.save()
		ingredient = Ingredient(recipe = recipe, name = 'Chocolate', quantity = 2, unit = 'l')
		ingredient.save()
		client = Client()
		response = client.get('/RecipeApp/recipes?id='+str(recipe.id))
		self.assertContains(response, 'Just throw everything to oven and see what happens!')	
		self.assertContains(response, 'Chocolate')