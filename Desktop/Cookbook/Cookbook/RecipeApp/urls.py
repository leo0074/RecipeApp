from django.urls import include, path
from django.contrib import admin
from RecipeApp.views import login_view, recipes_view, logout_view
urlpatterns = [
    path('login', login_view.login_page, name='login'),
	path('logout', logout_view.logout_page, name='logout'),
    path('recipes', recipes_view.recipes, name='recipes'),
    path('admin/', admin.site.urls),
]