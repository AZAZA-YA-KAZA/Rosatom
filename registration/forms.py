import re

from django import forms
from django.core.validators import RegexValidator


class RegForm(forms.Form):
    name = forms.CharField()
    fam = forms.CharField()
    login = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())
    phone_validator = RegexValidator(regex=r'^\+?1?\d{9,15}$')
    tel = forms.CharField(
        label='Телефон',
        validators=[phone_validator],  # Добавляем валидатор
        widget=forms.TextInput(attrs={'placeholder': 'Введите номер телефона'})
    )
    email = forms.EmailField()
