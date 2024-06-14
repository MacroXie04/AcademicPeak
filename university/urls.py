from django.urls import path
from university import views

urlpatterns = [
    path('', views.index, name='Translator'),
    path('api/', views.university_api, name='university_api'),
]