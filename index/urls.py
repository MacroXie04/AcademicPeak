# the urls.py for index
from django.urls import path
from index import views
from index.views import index

app_name = 'index'
urlpatterns = [
    path('', index.index, name='index'),
]

