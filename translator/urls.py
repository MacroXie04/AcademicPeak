# the urls.py for translator
from django.urls import path
from translator import views

urlpatterns = [
    path('', views.translator),
    path('api/', views.translate_api),
]