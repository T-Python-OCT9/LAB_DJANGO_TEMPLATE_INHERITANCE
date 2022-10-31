from django.urls import path
from . import views

app_name = "MyWebsite"

urlpatterns = [
    path('today/', views.theDate, name = "Date"),
    path('password/', views.passwordGenerator, name = "PassWord"),
    path('games/', views.favGames, name = "FavGames")
    
]


