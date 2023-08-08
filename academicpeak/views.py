from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.core.cache import cache
from academicpeak.models import University
from . import database
# Create your views here.

"""def mainpage(request):
    return render(request, 'google73e971ce68cd61bd.html')
"""

def mainpage(request):
    universities_rank = cache_university_ranking()
    return render(request, 'ranking.html', {'universities_rank': universities_rank})


def cache_university_ranking():
    universities_rank = cache.get('universities_rank')
    if universities_rank is None:
        universities_rank = database.return_university_dict()
        cache.set('universities_rank', universities_rank, timeout=None)
    return universities_rank
