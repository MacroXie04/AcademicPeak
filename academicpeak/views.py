import requests
import mistune
import os
import markdown
import commonmark
from academicpeak.code.Translate.AuthV3Util import addAuthParams
from django.shortcuts import render
from django.core.cache import cache
from .code import database
from django.conf import settings
from academicpeak.code.markdown import MarkdownDirectoryManager
from django.shortcuts import render
from django.http import JsonResponse
import openai

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hongzhe.settings')




def academic_peak_chat(request):
    if request.method == 'POST':
        input_text = request.POST.get('input_text')
        print(f'user_input: {input_text}')

        openai.api_key = ''

        # Constructing the prompt with academic instructions
        prompt = f"Academic Chat:\nUser: {input_text}\nAcademic Chat: Please provide a detailed and scholarly response discussing the topic: {input_text}\n"

        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=1024,  # You can adjust the length as needed
            temperature=0.7  # Adjust the temperature as needed
        )

        chatbot_response = response.choices[0].text.strip()
        return JsonResponse({'response': chatbot_response})

    return render(request, 'academicpeak_chat.html')


def cache_university_ranking():
    universities_rank = cache.get('universities_rank')
    if universities_rank is None:
        universities_rank = database.return_university_dict()
        cache.set('universities_rank', universities_rank, timeout=None)
    return universities_rank


def academic_peak_markdown(request):
    # Try to get folder_data from cache
    folder_data = cache.get('folder_data')

    if folder_data is None:
        markdown_manager = MarkdownDirectoryManager()
        folder_data = markdown_manager.get_folder_data()
        # Store folder_data in cache for 1 hour (in seconds)
        cache.set('folder_data', folder_data, 1)

    return render(request, 'academicpeak_markdown.html', {'folder_data': folder_data})


def academic_peak_markdown_reader(request, md_directory, md_name):
    # Construct the markdown file path based on directory and name
    markdown_file_path = os.path.join(settings.BASE_DIR, 'academicpeak', 'static', 'markdown', md_directory,
                                      f'{md_name}.md')

    if os.path.exists(markdown_file_path) and markdown_file_path.endswith('.md'):
        with open(markdown_file_path, 'r', encoding='utf-8') as f:
            markdown_content = f.read()

            # 使用 CommonMark-Py 渲染 Markdown 为 HTML
            html_content = commonmark.commonmark(markdown_content)

            return render(request, 'academicpeak_markdown_reader.html', {'markdown_content': html_content})
    else:
        print('Error: File not found.')
        return render(request, 'academicpeak_markdown_reader.html')


def academic_peak_scholar(request):
    return render(request, 'academicpeak_scholar.html')


def academic_peak_translate(request):
    translated_text = None
    if request.method == 'POST':
        source_text = request.POST.get('source_text', '')
        print(source_text)
        if source_text:
            translated_text = translator(source_text)
    return render(request, 'academicpeak_translate.html', {'translated_text': translated_text})


def translator(text):
    lang_form, lang_to = judge_language(text)
    if lang_form == 'unknown':
        return 'Error : Unknown UTF_8 character，我已经知道Bug出在哪里了，就是用户不输入正常文字，但是我不想改，因为我懒，等着哪天闲的没事给他改了'
    return generate_translation(text, lang_form, lang_to)


def judge_language(s: str) -> tuple[str, str] | str:
    # 找到第一个单词
    first_word = s.split()[0] if s else ""

    if not first_word:
        return 'unknown', 'unknown'

    for char in first_word:
        if '\u4e00' <= char <= '\u9fa5' or '\u3400' <= char <= '\u4dbf':
            return 'zh-CHS', 'en'
        elif '\u0000' <= char <= '\u007f':
            continue
        else:
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


def academic_peak_about(request):
    return render(request, 'academicpeak_about.html')
