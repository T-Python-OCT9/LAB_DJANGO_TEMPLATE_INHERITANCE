from django.urls import path
from . import views

urlpatterns = [ 
    path("home/", views.home, name="home"),
    path("random/password/", views.random_pass, name="random_pass"),
    path("games/favs/", views.game, name="game"),
    
]