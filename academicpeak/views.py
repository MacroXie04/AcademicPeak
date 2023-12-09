import requests
import mistune
import os
import markdown
import commonmark
from academicpeak.code.translator import translator
from django.shortcuts import render
from django.core.cache import cache
from .code import database
from django.conf import settings
from academicpeak.code.markdown import MarkdownDirectoryManager
from academicpeak.code.academy import AcademyDirectoryManager
from django.shortcuts import render
from django.http import JsonResponse

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hongzhe.settings')


def academic_peak_academy(request):
    # Try to get folder_data from cache
    academy_data = cache.get('academy_data')

    if academy_data is None:
        academy_manager = AcademyDirectoryManager()
        academy_data = academy_manager.get_folder_data()
        # Store academy_data in cache for 1 hour (in seconds)
        cache.set('academy_data', academy_data, 1)

    print(academy_data)

    return render(request, 'academicpeak_academy.html', {'folder_data': academy_data})


def academic_peak_academy_study(request, subject, item_code):
    return render(request, 'acaedmicpeak_academy_study.html',
                  context={'subject': subject, 'item_code': item_code})


def academic_peak_markdown(request):
    """Render markdown page"""

    # Try to get folder_data from cache
    folder_data = cache.get('folder_data')

    if folder_data is None:
        markdown_manager = MarkdownDirectoryManager()
        folder_data = markdown_manager.get_folder_data()
        cache.set('folder_data', folder_data, 15)

    return render(request, 'academicpeak_markdown.html', {'folder_data': folder_data})


def academic_peak_markdown_reader(request, md_directory, md_name):
    # Construct the markdown file path based on directory and name
    markdown_file_path = os.path.join(settings.BASE_DIR, 'academicpeak', 'static', 'markdown', md_directory,
                                      f'{md_name}.md')

    if os.path.exists(markdown_file_path) and markdown_file_path.endswith('.md'):
        with open(markdown_file_path, 'r', encoding='utf-8') as f:
            markdown_content = f.read()

            html_content = commonmark.commonmark(markdown_content)

            return render(request, 'academicpeak_markdown_reader.html',
                          {'markdown_content': html_content, 'file_name': md_name})
    else:
        print('Error: File not found.')
        return render(request, 'academicpeak_markdown_reader.html')


def academic_peak_translate(request):
    translated_text = None
    if request.method == 'POST':
        source_text = request.POST.get('source_text', '')
        if source_text:
            translated_text = translator(source_text)
    return render(request, 'academicpeak_translate.html',
                  {'translated_text': translated_text})


def academic_peak_mainpage(request):
    # return render(request, template_name='baidu_verify_codeva-l4eBn4mUtJ.html')
    return render(request, 'academicpeak_mainpage.html')


def academic_peak_legal(request):
    return render(request, 'academicpeak_legal.html')


def cache_university_ranking():
    """Cache the university ranking data."""
    universities_rank = cache.get('universities_rank')
    if universities_rank is None:
        universities_rank = database.return_university_dict()
        cache.set('universities_rank', universities_rank, timeout=15 * 60)
    return universities_rank


def academic_peak_university_ranking(request):
    """The function returns the ranking of universities."""
    universities_rank = cache_university_ranking()
    return render(request, 'academicpeak_ranking.html', {'universities_rank': universities_rank})


def academic_peak_fairness(request):
    return render(request, 'academicpeak_fairness.html')


def academic_peak_about(request):
    return render(request, 'academicpeak_about.html')


def academic_peak_gratitude(request):
    return render(request, template_name='academicpeak_gratitude.html')
