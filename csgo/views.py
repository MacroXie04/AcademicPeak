from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def mainpage(request):
    return HttpResponse ("This is the main page of csgo")
