import os.path

from django.conf import settings

def handle_uploaded_file(f):
    abs_file_path = os.path.join(settings.MEDIA_ROOT, f.name)
    with open(abs_file_path, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

