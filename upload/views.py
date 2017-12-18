from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from .forms import UploadFileForm
from .handlers import handle_uploaded_file


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            file_name = request.FILES['uploading_file'].name
            handle_uploaded_file(request.FILES['uploading_file'])
            return HttpResponse("{file_name}.".format(file_name=file_name))
    else:
        form = UploadFileForm()
    return render(request, 'upload/upload.html', {'form': form})
