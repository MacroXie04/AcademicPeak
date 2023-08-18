from django.urls import path
from csgo import views

urlpatterns = [
    path('', views.mainpage, name='csgo'),

]