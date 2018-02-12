from django.urls import include, path
from django.contrib import admin
from RecipeApp.views import login_view
urlpatterns = [
    path('login', login_view.login, name='login'),
    path('admin/', admin.site.urls),
]