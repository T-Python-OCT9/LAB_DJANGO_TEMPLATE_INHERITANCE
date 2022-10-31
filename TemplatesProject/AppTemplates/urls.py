from django.urls import path     
from . import views


app_name = 'AppTemplate'
urlpatterns = [
    path('today/', views.Today, name="Today"),
    path('random/password/', views.Password, name="Password"),
    ]