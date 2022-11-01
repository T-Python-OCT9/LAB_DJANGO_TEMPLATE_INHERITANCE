urlpatterns = [
    path('today/', views.today, name="today"),
    path('random/password/', views.PASS, name="password"),
    path('favs/games/', views.FavoriteGames , name="games"),
]