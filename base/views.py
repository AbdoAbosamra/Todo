from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView ,UpdateView
from django.urls import reverse_lazy

from pip._internal.utils.misc import ask

from .models import Task
# Create your views here.

class TaskList(ListView):
    model = Task
    context_object_name = 'tasks' # we change the name of queryst of objects in our models.

class TaskDetail(DetailView):
    model = Task
    context_object_name = 'task'

class TaskCreate(CreateView):
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('tasks') # this is for redirect after created action.

class TaskUpdate(UpdateView):
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('tasks')  # this is for redirect after created action.

