from django import forms
from .models import Profile,Photo


class NewProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['person']

class NewPhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        exclude = ['person']


