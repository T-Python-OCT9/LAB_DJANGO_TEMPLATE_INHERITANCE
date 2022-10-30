from unicodedata import name
from. import views
from django.urls import path

app_name="pageOne"


urlpatterns = [
    path('one/',views.pageOne,name="pageOne"),
    path('two/',views.pageTwo,name="pageTwo"),
    path('three',views.pageThree,name="pageThree")
]