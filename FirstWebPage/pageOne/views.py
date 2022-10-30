from django.shortcuts import render
from django.http import HttpRequest



def pageOne(request:HttpRequest):
    return render(request,'pageOne/pageOne.html')

def pageTwo(request:HttpRequest):
    return render(request,'pageOne/pageTwo.html')

def pageThree(request:HttpRequest):
    return render(request,'pageOne/pageThree.html')

# Create your views here.
