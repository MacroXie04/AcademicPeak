# the urls.py for academicpeak

from django.urls import path
from academicpeak import views

urlpatterns = [
    path('', views.academic_peak_mainpage, name='academic_peak_mainpage'),
    path('ranking/', views.academic_peak_university_ranking, name='academic_peak_university_ranking'),
    path('about/', views.academic_peak_about, name='academic_peak_about'),
    path('contact/', views.academic_peak_contact, name='academic_peak_contact'),
    path('fairness/', views.academic_peak_fairness, name='academic_peak_fairness'),
    path('legal/', views.academic_peak_legal, name='academic_peak_legal'),
    path('translate/', views.translate, name='academic_peak_translate'),
    path('display/markdown/<str:file_name>/', views.display_markdown, name='display_markdown'),


]
