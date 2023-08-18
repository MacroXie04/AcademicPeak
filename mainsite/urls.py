# the urls.py for mainsite
from django.urls import path
from django.urls import include
from mainsite import views


urlpatterns = [
    path('', views.mainpage, name='mainpage'),
    path('about/', views.about, name='about'),
    path('love/', views.love, name='love'),
]
