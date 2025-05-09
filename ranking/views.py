from django.shortcuts import render

def ranking_index(request):
    return render(request, 'index_ranking.html')


def ranking_search(request):
    return render(request, 'ranking_page/search_ranking.html')

def ranking_ranking(request):
    return render(request, 'ranking_page/ranking_ranking.html')


