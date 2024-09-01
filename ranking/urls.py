# the urls.py for ranking
from django.urls import path
from ranking import views

urlpatterns = [
    path('', views.ranking_index, name='ranking_index'),

    path('login/', views.ranking_login, name='ranking_login'),

    path('search/', views.ranking_search, name='ranking_search'),

    path('ranking/', views.ranking_ranking, name='ranking_ranking'),



]