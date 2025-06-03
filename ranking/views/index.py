from django.shortcuts import render

def ranking_index(request):
    return render(request, 'ranking_index.html', {"active_page": "ranking_index"})