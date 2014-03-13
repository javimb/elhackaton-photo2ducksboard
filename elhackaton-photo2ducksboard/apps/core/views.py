from django.shortcuts import render, redirect

from .models import Photo
from .forms import PhotoForm


def index(request):
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            photo = form.save()
            photo.send_to_ducksboard()
            return redirect('/')
    else:
        form = PhotoForm()
    photos = Photo.objects.get_all_photos()
    return render(request, 'core/index.html', {'form': form,
        'photos': photos})