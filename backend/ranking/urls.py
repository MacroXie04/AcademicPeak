# the urls.py for ranking
from .views import index
from django.urls import path
from ranking import views

app_name = 'ranking'
urlpatterns = [
    path('', index.ranking_index, name='ranking_index'),
]