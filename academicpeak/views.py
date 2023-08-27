import requests
import os
import markdown2
from academicpeak.Translate.AuthV3Util import addAuthParams
from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.core.cache import cache
from django.conf import settings
from academicpeak.models import University
from . import database
APP_KEY = '3826d1e6c939ecaf'
APP_SECRET = 'lszlbHaIdLKlk6kTU31e9YNj57BcdxAM'

def cache_university_ranking():
    universities_rank = cache.get('universities_rank')
    if universities_rank is None:
        universities_rank = database.return_university_dict()
        cache.set('universities_rank', universities_rank, timeout=None)
    return universities_rank


def display_markdown(request, file_name):
    markdown_file_path = os.path.join(settings.BASE_DIR, 'academicpeak', 'static', 'markdown', file_name)
    markdown_file_path = r'C:\Users\xieho\PycharmProjects\hongzhe.site\academicpeak\static\markdown\test.md'
    print(markdown_file_path)
    if os.path.exists(markdown_file_path) and markdown_file_path.endswith('.md'):
        with open(markdown_file_path, 'r', encoding='utf-8') as f:
            markdown_content = f.read()
            markdown_content = markdown2.markdown(markdown_content)
            return render(request, 'academicpeak_md.html', {'markdown_content': markdown_content})
    else:
        print('Error: File not found.')
        return render(request, 'academicpeak_md.html')

def translate(request):
    translated_text = None
    if request.method == 'POST':
        source_text = request.POST.get('source_text', '')
        if source_text:
            translated_text = translator(source_text)
    return render(request, 'academicpeak_translate.html', {'translated_text': translated_text})

def translator(text):
    lang_form, lang_to = judge_language(text)
    if lang_form == 'unknown':
        return 'Error : Unknown UTF_8 character，我已经知道Bug出在哪里了，但是我不想改，因为我懒，等着哪天闲的没事给他改了'
    return generate_translation(text, lang_form, lang_to)

def judge_language(s: str) -> tuple[str, str] | str:
    # 检查字符串中的每个字符
    for char in s:
        # 判断是否是中文
        if '\u4e00' <= char <= '\u9fa5' or '\u3400' <= char <= '\u4dbf':
            return 'zh-CHS', 'en'
        # 判断是否是英文
        elif '\u0000' <= char <= '\u007f':
            continue
        else:
            # 如果不在中英文字符范围内，则返回未知
            return 'unknown', 'unknown'
    return 'en', 'zh-CHS'

def generate_translation(text, lang_from, lang_to):
    data = {'q': text, 'from': lang_from, 'to': lang_to}
    addAuthParams(APP_KEY, APP_SECRET, data)
    header = {'Content-Type': 'application/x-www-form-urlencoded'}
    res = doCall('https://openapi.youdao.com/api', header, data, 'post')
    return res.json()['translation'][0]


def doCall(url, header, params, method):
    if 'get' == method:
        return requests.get(url, params)
    elif 'post' == method:
        return requests.post(url, params, header)




def academic_peak_mainpage(request):
    return render(request, 'academicpeak_mainpage.html')

def academic_peak_legal(request):
    return render(request, 'academicpeak_legal.html')

def academic_peak_university_ranking(request):
    universities_rank = cache_university_ranking()
    return render(request, 'academicpeak_ranking.html', {'universities_rank': universities_rank})


def academic_peak_fairness(request):
    return render(request, 'academicpeak_fairness.html')


def academic_peak_contact(request):
    return render(request, 'academicpeak_contact.html')


def academic_peak_about(request):
    return render(request, 'academicpeak_about.html')











