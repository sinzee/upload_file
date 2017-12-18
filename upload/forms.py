from django import forms

class UploadFileForm(forms.Form):
    uploading_file = forms.FileField(
        label='Select a file'
    )
