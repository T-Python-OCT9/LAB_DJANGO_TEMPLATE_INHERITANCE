from django.urls import path     
from . import views

app_name = 'AppTemplate'
urlpatterns = [
    path('today/', views.today, name="today"),
    path('random/password/', views.password, name="password"),
    path('favs/games/', views.favGames, name="games"),
]