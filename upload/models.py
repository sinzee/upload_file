from django.db import models


class UploadedFiles(models.Model):


    uploaded_file = models.FileField(upload_to='files/%Y/%m/%d')


