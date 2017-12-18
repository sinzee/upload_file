from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from .forms import UploadFileForm
from .models import UploadedFiles


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            new_file = UploadedFiles(uploaded_file=request.FILES['uploading_file'])
            new_file.save()
            file_name = request.FILES['uploading_file'].name
            return HttpResponse("{file_name}.".format(file_name=file_name))
    else:
        form = UploadFileForm()
    return render(request, 'upload/upload.html', {'form': form})
