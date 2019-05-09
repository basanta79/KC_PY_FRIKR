from django.contrib.auth import authenticate, login as django_login
from django.shortcuts import render, redirect
from django.contrib import messages


# Create your views here.

def login(request):
    if request.method == 'POST':
        username = request.POST['usr']
        password = request.POST['pwd']
        user = authenticate(username=username, password=password)
        if user is None:
            messages.error(request, 'usuario/contraseña incorrecto')
        else:
            django_login(request, user)
            return redirect('home')
    return render(request, 'users/login.html')