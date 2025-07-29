from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Note


class CustomRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['username'].help_text = '4 letters at least'

        self.fields['password1'].help_text = ''
        self.fields['password2'].help_text = ''

class NoteUploadForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'description', 'subject', 'tags']
        help_texts = {
            'tags' : None
        }