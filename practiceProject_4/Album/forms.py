from django import forms
from . import models


class AlbumModelForm(forms.ModelForm):
    class Meta:
        model=models.AlbumForm
        fields='__all__'