from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

@login_required
def recipes(request):
    return render(request, 'RecipeApp/recipes.html')