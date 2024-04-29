import os
import commonmark
from django.conf import settings
from django.core.cache import cache
from django.shortcuts import render
from academicpeak.code.academy import AcademyDirectoryManager
from academicpeak.code.markdown import MarkdownDirectoryManager
from academicpeak.code.translator import translator
from .code import database
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hongzhe.settings')


def academic_peak_academy(request):
    """Returns the rendered HTML view of the Academic Peak Academy page"""
    # Try to get folder_data from cache
    academy_data = cache.get('academy_data')
    if academy_data is None:
        # Reload data to cache
        academy_manager = AcademyDirectoryManager()
        academy_data = academy_manager.get_folder_data()
        # Store academy_data in cache for 1 hour (in seconds)
        cache.set('academy_data', academy_data, 1)
    return render(request, 'academicpeak_academy.html', {'folder_data': academy_data})


def academic_peak_academy_study(request, subject, item_code):
    """Render video page"""
    return render(request, 'acaedmicpeak_academy_study.html',
                  context={'subject': subject, 'item_code': item_code})


def academic_peak_markdown(request):
    """Render markdown page"""
    # Try to get folder from cache
    folder = cache.get('folder')
    if folder is None:
        markdown_manager = MarkdownDirectoryManager()
        folder = markdown_manager.get_folder()  # Assuming this returns a list of folder names
        cache.set('folder', folder, 15)  # Cache the result for 15 seconds
    print(folder)
    return render(request, 'academicpeak_markdown.html', {'folder': folder})


def academic_peak_markdown_part(request, md_directory):
    # Retrieve folder data from cache or regenerate it if not available
    folder_data = cache.get('folder_data')
    if folder_data is None:
        markdown_manager = MarkdownDirectoryManager()
        folder_data = markdown_manager.get_folder_data()
        cache.set('folder_data', folder_data, 15)  # Cache the data for 15 seconds

    # Initialize an empty list for the items
    item_list = []

    # Find the matching directory and its items
    for folder in folder_data:
        if folder['name'] == md_directory:
            item_list = folder['items']
            break  # Break the loop once the matching directory is found

    print(item_list)
    print(md_directory)
    # Render the template with the directory name and its corresponding items
    return render(request, 'academicpeak_markdown_part.html', {
        'directory_name': md_directory,
        'folder_data': item_list
    })



def academic_peak_markdown_reader(request, md_directory, md_name):
    """Process Markdown into html and return it for display"""
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
        return render(request, 'academicpeak_markdown_reader.html')


def academic_peak_translate(request):
    """Process User input from POST request and Translate the text by Youdao API"""
    source_text = None
    translated_text = None
    if request.method == 'POST':
        source_text = request.POST.get('source_text', '')
        if source_text:
            translated_text = translator(source_text)
    return render(request, 'academicpeak_translate.html',
                  {'translated_text': translated_text, 'source_text': source_text})


def academic_peak_mainpage(request):
    """Main page of AcademicPeak"""
    return render(request, 'academicpeak_mainpage.html')


def academic_peak_legal(request):
    return render(request, 'academicpeak_legal.html')


def cache_university_ranking():
    """Cache the university ranking data."""
    universities_rank = cache.get('universities_rank')
    if universities_rank is None:
        universities_rank = database.return_university_dict()
        cache.set('universities_rank', universities_rank, timeout=5)
    return universities_rank

def academic_peak_university_ranking(request):
    """Returns the ranking of universities."""
    universities_rank = cache_university_ranking()
    return render(request, 'academicpeak_ranking.html', {'universities_rank': universities_rank})


def academic_peak_fairness(request):
    """Returns the fairness of universities."""
    return render(request, 'academicpeak_fairness.html')


def academic_peak_about(request):
    """Returns the about page of AcademicPeak."""
    return render(request, 'academicpeak_about.html')


def academic_peak_gratitude(request):
    """Returns the gratitude page of AcademicPeak."""
    return render(request, template_name='academicpeak_gratitude.html')