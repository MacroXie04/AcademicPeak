# the urls.py for translator

from django.urls import path
from translator import views

urlpatterns = [
    path('', views.translate, name='translator'),
]