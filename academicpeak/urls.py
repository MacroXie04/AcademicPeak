# the urls.py for academicpeak
from django.urls import path
from academicpeak import views

urlpatterns = [
    # index page
    path('', views.academic_peak_mainpage, name='academic_peak_mainpage'),

    # Academic peak World University Ranking 2024
    path('ranking/', views.academic_peak_university_ranking, name='academic_peak_university_ranking'),

    # Translator
    path('translate/', views.academic_peak_translate, name='academic_peak_translate'),

    # Markdown center
    path('markdown/', views.academic_peak_markdown, name="academic_peak_markdown"),
    path('markdown/<str:md_directory>/', views.academic_peak_markdown_part, name='markdown_part'),
    path('markdown/<str:md_directory>/<str:md_name>/', views.academic_peak_markdown_reader,
         name='academic_peak_markdown_reader'),

    path('academy/', views.academic_peak_academy, name='academic_peak_academy'),
    path('academy/<str:subject>/<str:item_code>/', views.academic_peak_academy_study,
         name='academic_peak_academy_study'),

    # Other About web pages
    path('about/', views.academic_peak_about, name='academic_peak_about'),
    path('fairness/', views.academic_peak_fairness, name='academic_peak_fairness'),
    path('legal/', views.academic_peak_legal, name='academic_peak_legal'),
    path('gratitude/', views.academic_peak_gratitude, name='academic_peak_gratitude'),

]
