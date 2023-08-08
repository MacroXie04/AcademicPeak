from django.shortcuts import render

# Create your views here.

def mainpage(request):
    return render(request, 'java_main.html')

def introduction(request):
    return render(request, 'introductory_java_language_features.html')

def classes_objects(request):
    return render(request, 'classes&objects.html')

def inheritance_polymorphism(request):
    return render(request, 'inheritance&polymorphism.html')

def some_standard_classes(request):
    return render(request, 'some_standard_classes.html')

def arrays(request):
    container = '{{3,4,5},{6,7,8}}'
    return render(request, 'arrays&arraylists.html', {'container': container})

def recursion(request):
    return render(request, 'recursion.html')