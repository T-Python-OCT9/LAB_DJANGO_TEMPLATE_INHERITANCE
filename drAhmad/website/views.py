from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from datetime import date
import random
import string

# Create your views here.



def today(request:HttpRequest):
    context = {
        'today':date.today(),
    }
    return render(request,'TEMPLATE_INHERITANCE_APP/today.html',context)

def password(request:HttpRequest):
    context = {
        'password' : ''.join(random.choice(string.printable) for i in range(15))
    }
    return render(request,'TEMPLATE_INHERITANCE_APP/password.html',context)

def favGames(request:HttpRequest):
    context ={
        'fav': ["8ball" , "PUBG Mobile" , "Card Thief" , "Sega Heroes" , "Call of Duty"]
    }
    return render(request,'TEMPLATE_INHERITANCE_APP/favGames.html',context)
