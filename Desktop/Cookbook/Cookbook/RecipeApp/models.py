from django.db import models
from django.contrib.auth.models import User

class Recipe(models.Model):
	owner = models.ForeignKey(User, on_delete=models.CASCADE)
	recipe_text = models.TextField()
	created_date = models.DateTimeField()


class Ingredient(models.Model):
	recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
	name = models.TextField()
	quantity = models.FloatField()
	unit = models.TextField()

class Review(models.Model):
	writer = models.ForeignKey(User, on_delete=models.CASCADE)
	recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
	review_text = models.TextField()