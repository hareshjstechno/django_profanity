from django.shortcuts import render,redirect
from django.contrib import messages
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from .forms import DocumentForm
def model_form_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS,'Your Data Has Been Submited........')
    else:
        form = DocumentForm()
    return render(request, 'model_form_upload.html', {
        'form': form
    })

