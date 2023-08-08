from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.shortcuts import redirect

# Create your views here.

def about(request):
    return render(request, 'about.html')

def mainpage(request):
    return render(request, 'main.html')

def love(request):
    return render(request, 'love.html')