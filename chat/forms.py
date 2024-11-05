from django import forms
from django.db.models import CharField


class ChatForm(forms.Form):
    text = forms.CharField(max_length=1000, widget=forms.TextInput(attrs={'style': 'width: 95%;'}))
