# the urls.py for ranking
from django.urls import path
from ranking import views

urlpatterns = [
    path('', views.ranking_index),

]