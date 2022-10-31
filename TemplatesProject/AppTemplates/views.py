from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from datetime import date
import random
import string
# Create your views here.

def Today(request:HttpRequest):
    context = {
        'today':date.today(),
    }
    return render(request,'AppTemplate/Today.html',context)

def Password(request:HttpRequest):
    context = {
        'password' : ''.join(random.choice(string.printable) for i in range(8))
    }
    return render(request,'AppTemplate/Password.html',context)

def FavoriteGames(request:HttpRequest):
    context ={
        'fav': ["babgi" , "Pubge Mobile" , "Fort nite" , "Call of Duty" , "we play"]
    }
    return render(request,'AppTemplate/FavoriteGames.html',context)