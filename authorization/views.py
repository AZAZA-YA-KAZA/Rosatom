from django.core.files.base import equals_lf
from django.db import models, IntegrityError
from django.shortcuts import render, redirect

from django.contrib.auth.hashers import check_password
from authorization.forms import AuthForm
from authorization.models import Auth


def authotiz(request):
    if request.method == 'POST':
        form = AuthForm(request.POST)
        if form.is_valid():
            login = form.cleaned_data['login']
            password = form.cleaned_data['password']
            try:
                user = Auth.objects.get(login=login)
                print(password, user.password)
                if password == user.password:
                    return redirect('/reg')  # Замените на вашу страницу успеха
                else:
                    error_message = "Пользовательские данные некорректны"
                    return render(request, 'authorization/auth.html', {'form': form, 'error_message': error_message})
            except Auth.DoesNotExist:
                error_message = "Пользователя с таким логином не существует."
                return render(request, 'authorization/auth.html', {'form': form, 'error_message': error_message})
    else:
        form = AuthForm()
    return render(request, 'authorization/auth.html', {'form': form})