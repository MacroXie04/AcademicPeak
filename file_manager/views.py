from django.shortcuts import render

# Create your views here.
# file_manager/views.py

from django.shortcuts import render, redirect
from django.http import FileResponse
from .models import UploadedFile
from .forms import UploadFileForm


def file_list(request):
    files = UploadedFile.objects.all()
    return render(request, 'file_list.html', {'files': files})

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('file_list')
    else:
        form = UploadFileForm()
    return render(request, 'upload_file.html', {'form': form})

def download_file(request, file_id):
    uploaded_file = UploadedFile.objects.get(pk=file_id)
    file_path = uploaded_file.file.path
    response = FileResponse(open(file_path, 'rb'))
    response['Content-Disposition'] = f'attachment; filename="{uploaded_file.file.name}"'
    return response
