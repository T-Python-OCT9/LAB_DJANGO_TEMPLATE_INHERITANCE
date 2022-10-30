from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from datetime import date
import string
from random import choice
import random


# Create your views here.

def home(request: HttpRequest):

    msg = " "

    return render(request, "info2/index.html", {"welcom" : msg} )


def random_pass(request: HttpRequest):

    p = ""
    char = list(string.ascii_letters + string.digits + '!@#$%^&*')
    
    while len(p) <= 8:
        p += random.choice(char)
    
    
    return render(request, 'info2/random.html', {"pass" : p}) 





list_of_game =["puzzles","crush","solitaire","farm"]

def game(request: HttpRequest):
    
    #for i in list_of_game:
      #output += list_of_game[i]
     

    return render(request, 'info2/game.html', {"game" : list_of_game})

