from turtle import home
from django.urls import path
from .views import homeView,todayView, randomPasswordView, favoriteGamesView

app_name = 'website'

urlpatterns = [
    path('home/', homeView, name='home'),
    path('today/', todayView, name='today'),
    path('random/password/', randomPasswordView, name='random_password'),
    path('favs/games/', favoriteGamesView, name='favorite_games'),
]