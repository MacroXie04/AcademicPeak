from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.core.cache import cache
from academicpeak.models import University
from . import database


def academic_peak_mainpage(request):
    return render(request, 'academicpeak_mainpage.html')


def academic_peak_university_ranking(request):
    universities_rank = cache_university_ranking()
    return render(request, 'academicpeak_ranking.html', {'universities_rank': universities_rank})


def academic_peak_contact(request):
    return render(request, 'academicpeak_contact.html')


def academic_peak_about(request):
    return render(request, 'academicpeak_about.html')


def cache_university_ranking():
    universities_rank = cache.get('universities_rank')
    if universities_rank is None:
        universities_rank = database.return_university_dict()
        cache.set('universities_rank', universities_rank, timeout=None)
    return universities_rank
