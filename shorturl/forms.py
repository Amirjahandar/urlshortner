from dataclasses import fields

from django import forms
from .models import ShortUrl


class CreateNewShortUrl(forms.ModelForm):

    class Meta:
        model = ShortUrl
        fields = ['original_url']

        widgets = {
            'original_url': forms.TextInput(attrs={'class': 'form-control'})
        }
