from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core import serializers
import datetime
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from .forms import *

# tampilan halaman utama
@login_required(login_url='/todolist/login/')
def show_todolist(request):
    nama = request.user
    data = request.user.user_todolist.all()
    context = {
        'nama' : nama,
        'data': data
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
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('todolist:login')
    
    form = UserCreationForm()
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

@login_required(login_url='/todolist/login/')
def show_todolist_ajax(request):
    data = request.user.user_todolist.all()
    context = {
    'data' : data,
    }
    return render(request, "todolist_ajax.html", context)

def show_json(request):
    data = request.user.user_todolist.all()
    return HttpResponse(serializers.serialize("json", data ), content_type="application/json")

def add(request):
    print(request.POST)
    print(request.user)
    if request.method == 'POST':
        print(request.POST)
        
        user = request.user
        title = request.POST.get('title')
        description = request.POST.get('description')
        form = Task(user= user, title=title, description=description)
        form.save()
        return HttpResponse(status=200)
    return HttpResponseNotFound()

