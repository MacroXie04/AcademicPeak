from django.shortcuts import render

def ranking_index(request):
    return render(request, 'index_ranking.html', {"active_page": "ranking_index"})