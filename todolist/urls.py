from unicodedata import name
from django.urls import path
from todolist.views import *

app_name = 'todolist'

urlpatterns = [
    path('', show_todolist, name='showtodolist'), #url halaman utama
    path('create_task/', create_task, name='create_task'), #url pembuatan task
    path('register/', register, name='register'), #url register
    path('login/', login_user, name='login'), #url login
    path('logout/', logout_user, name='logout'), #url logout
    path('ajax/', show_todolist_ajax, name='show_todolist_ajax'), #url ajax
    path('ajax/json/', show_json, name='show_json'), #url json
    path('ajax/add/', add, name='add') #url submit form

]