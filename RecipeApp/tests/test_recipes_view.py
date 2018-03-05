from django.test import TestCase
from RecipeApp.models import Recipe
from django.test import Client
from django.utils import timezone
from django.contrib.auth.models import User
class QuestionIndexViewTests(TestCase):
	def test_no_recipes(self):
		client = Client()
		response = client.get('/RecipeApp/recipes')
		self.assertContains(response, 'No recipes are available.')
		
	def test_with_2_recipes(self):
		owner = User.objects.create_user('leo0074', 'leo.palkio@gmail.com' , 'Supaersecretpassword')
		recipe1 = Recipe(owner = owner, name = 'Mudacake', created_date = timezone.now())
		recipe2 = Recipe(owner = owner, name = 'Chocolate cake', created_date = timezone.now())
		recipe1.save()
		recipe2.save()
		client = Client()
		response = client.get('/RecipeApp/recipes')
		self.assertContains(response, 'Mudacake')	
		self.assertContains(response, 'Chocolate cake')	