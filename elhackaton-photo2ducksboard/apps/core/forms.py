from django import forms

from .models import Photo


class PhotoForm(forms.ModelForm):
    image = forms.ImageField(label='Upload your photo:')

    class Meta:
        model = Photo
        fields = ('image',)