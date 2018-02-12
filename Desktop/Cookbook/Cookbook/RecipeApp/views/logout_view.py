from django.shortcuts import render
from django.contrib.auth import logout

def logout_page(request):
	logout(request)
	return render(request, 'RecipeApp/logout.html')
	