# the urls.py for java
from django.urls import path
from . import views

urlpatterns = [
    path('', views.mainpage, name='java_main'),
    path('introduction/', views.introduction, name='java_introduction'),
    path('classes_objects/', views.classes_objects, name='java_classes_objects'),
    path('inheritance_polymorphism/', views.inheritance_polymorphism, name='java_inheritance_polymorphism'),
    path('some_standard_classes/', views.some_standard_classes, name='java_some_standard_classes'),
    path('arrays/', views.arrays, name='java_arrays'),
    path('recursion/', views.recursion, name='java_recursion'),
]
