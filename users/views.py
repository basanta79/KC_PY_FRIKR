from django.contrib.auth import authenticate, login as django_login, logout as django_logout
from django.shortcuts import render, redirect
from django.contrib import messages


# Create your views here.
from users.forms import LoginForm


def login(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('usr')
            password = form.cleaned_data.get('pwd')
            user = authenticate(username=username, password=password)
            if user is None:
                messages.error(request, 'usuario/contraseña incorrecto')
            else:
                django_login(request, user)
                return redirect('home')
    else:
        form = LoginForm()

    context = { 'form': form }
    return render(request, 'users/login.html', context)


def logout(request):
    django_logout(request)
    return redirect('login')

