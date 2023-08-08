# the urls.py for mainsite
from django.urls import path
from django.urls import include
from mainsite import views


urlpatterns = [
    path('', views.mainpage),
    path('about/', views.about),
    path('love/', views.love),
]
