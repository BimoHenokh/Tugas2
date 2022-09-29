from django.urls import path
from todolist.views import *

app_name = 'todolist'

urlpatterns = [
    # path('html/', show_html, name='show_html'),
    path('', show_todolist, name='showtodolist'),
    path('create_task/', create_task, name='create_task'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),

]