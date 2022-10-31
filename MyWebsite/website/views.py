import string
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from datetime import date
import random , string 



def home_view (request : HttpRequest) :
    return render( request,'website/home.html')

def today_View(request: HttpRequest):
    context = {'date': date.today}
    return render(request, 'website/date.html', context)

def random_Password_View(request: HttpRequest):
    types_of_password = string.ascii_lowercase + string.ascii_uppercase + string.digits
    password = ''.join(random.choice(types_of_password) for i in range(13))
    context = {'password': password}
    return render(request, 'website/password.html', context)


def favorite_Games_View(request: HttpRequest):
    favorite_games = ['Dota2', 'World of warcraft', 'Chess']
    context = {'favorite_games' : favorite_games}
    return render(request, 'website/games.html', context)
# Create your views here.
