# the urls.py for academicpeak

from django.urls import path
from academicpeak import views

urlpatterns = [
    path('', views.academic_peak_mainpage, name='academic_peak_mainpage'),
    path('ranking/', views.academic_peak_university_ranking, name='academic_peak_university_ranking'),
    path('about/', views.academic_peak_about, name='academic_peak_about'),
    path('fairness/', views.academic_peak_fairness, name='academic_peak_fairness'),
    path('legal/', views.academic_peak_legal, name='academic_peak_legal'),
    path('translate/', views.academic_peak_translate, name='academic_peak_translate'),
    path("markdown/", views.academic_peak_markdown, name="academic_peak_markdown"),
    path('scholar/', views.academic_peak_scholar, name='academic_peak_scholar'),
    path('markdown/<str:md_directory>/<str:md_name>/', views.academic_peak_markdown_reader, name='academic_peak_markdown_reader'),


]
