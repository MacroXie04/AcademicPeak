from django.shortcuts import render

def ranking_index(request):
    return render(request, 'index_ranking.html')

def ranking_login(request):
    return render(request, 'user_page/login_ranking.html')


def ranking_search(request):
    return render(request, 'ranking_page/search_ranking.html')

def ranking_ranking(request):
    return render(request, 'ranking_page/ranking_ranking.html')


