from . import models
from django import forms
class MusicianModelForm(forms.ModelForm):
    class Meta:
        model=models.MusicianForm
        fields='__all__'