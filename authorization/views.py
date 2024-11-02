from django.db import models, IntegrityError
from django.shortcuts import render, redirect

from authorization.forms import AuthForm
from authorization.models import Auth

def authotiz(request):
    if request.method == 'POST':
        form = AuthForm(request.POST)
        if form.is_valid():
            login = form.cleaned_data['login']
            password = form.cleaned_data['password']
            try:
                Auth.objects.create(login=login, password=password)
                return redirect('/auth')  # Замените на вашу страницу успеха
            except IntegrityError:
                error_message = "Пользователь с таким логином уже существует."
                return render(request, 'authorization/auth.html', {'form': form, 'error_message': error_message})
    else:
        form = AuthForm()
    return render(request, 'authorization/auth.html', {'form': form})