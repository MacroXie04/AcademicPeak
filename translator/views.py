from django.shortcuts import render
from django.http import JsonResponse
from translator.code.translator import Translator
from django.views.decorators.csrf import csrf_exempt

def translator(request):
    return render(request, 'translator.html')

@csrf_exempt
def translate_api(request):
    if request.method == 'POST':
        text = request.POST.get('text', '')
        result = Translator.translate(text)
        return JsonResponse({
            'original': 'text',
            'translation': 'test translation',
            'language': 'lang_from',
        })