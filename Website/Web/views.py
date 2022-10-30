import numbers
from secrets import choice
import string
from django.shortcuts import render
from django.http import HttpRequest , HttpResponse
from datetime import date
import random
# Create your views here.

def tody_date(request : HttpRequest):
   
    context = {"currentDate" : date.today()}
    return render( request,"Website/todaydate.html",context)



def random_Pass(request : HttpRequest):

  characters = random.choices(string.ascii_letters + string.digits + string.punctuation , k=15) 
  password = ''.join(characters)
  return render(request , "Website/pass.html" , {"pass" : password})
  

def fav_Games(request : HttpRequest):
    context = { "favGame":["super mario" , "crash bandicoot" ,"pepsiman"] }
    return render (request , "Website/favGame.html" , context)