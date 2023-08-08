from django.shortcuts import render
from django.http import HttpResponse
import requests
from django.http import JsonResponse
from translator.utils.AuthV3Util import addAuthParams
APP_KEY = '3826d1e6c939ecaf'
APP_SECRET = 'lszlbHaIdLKlk6kTU31e9YNj57BcdxAM'


def translate(request):
    translated_text = None

    if request.method == 'POST':
        source_text = request.POST.get('source_text', '')
        if source_text:
            translated_text = translator(source_text)
    return render(request, 'translate.html', {'translated_text': translated_text})



def translator(text):
    lang_form, lang_to = judge_language(text)
    if lang_form == 'unknown':
        return 'Error : Unknown UTF_8 character'
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


# 调试用接口
"""
if __name__ == '__main__':
    print(translator('Hello'))
"""
