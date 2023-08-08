# the urls.py for academicpeak

from django.urls import path
from academicpeak import views

urlpatterns = [
    path('', views.mainpage),
]