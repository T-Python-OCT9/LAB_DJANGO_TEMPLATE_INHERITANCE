from django.urls import  path
from .views import home_view, today_View , random_Password_View,favorite_Games_View


app_name = 'website'

urlpatterns = [
    path ('home/',home_view, name = 'home'),
    path('today/', today_View, name='today'),
    path('random/password/', random_Password_View, name='random_password'),
    path('favs/games/', favorite_Games_View, name='games'),
]