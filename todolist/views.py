from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import *

# tampilan halaman utama
@login_required(login_url='/todolist/login/')
def show_todolist(request):
    nama = request.user
    context = {
        'nama': nama
    }
    return render(request, "todolist.html", context)

# halaman membuat task
@login_required(login_url='/todolist/login/')
def create_task(request):
    if request.method == 'POST':
        form = TodolistModelForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('todolist:showtodolist')
        
    form = TodolistModelForm()
    nama = request.user
    context = {
        'form':form,
        'nama':nama
        }
    return render(request, 'form.html', context)

# halaman registrasi user
def register(request):
    form = UserCreationForm()
    # form_name = form.

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('todolist:login')
    
    context = {'form':form,}
    return render(request, 'register.html', context)

# halaman login user
def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user) 
            response = HttpResponseRedirect(reverse("todolist:showtodolist")) 
            response.set_cookie('last_login', str(datetime.datetime.now())) 
            return response
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)

# halaman logout
def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('todolist:login'))
    response.delete_cookie('last_login')
    return redirect('todolist:login')