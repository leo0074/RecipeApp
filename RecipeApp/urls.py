from django.urls import include, path
from django.contrib import admin
from RecipeApp.views import login_view, recipes_view, logout_view, register_view, new_recipe_view
urlpatterns = [
    path('login', login_view.login_page, name='login'),
	path('logout', logout_view.logout_page, name='logout'),
	path('register', register_view.register, name='register'),
    path('recipes', recipes_view.recipes, name='recipes'),
    path('new_recipe', new_recipe_view.new_recipe, name='new_recipe'),
	path('admin/', admin.site.urls),
]