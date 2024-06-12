from django.shortcuts import render
from django.http import JsonResponse

def index(request):
    return render(request, 'translator/index.html')

def translate(request):


    return