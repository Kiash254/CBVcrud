from pyexpat import model
from statistics import mode
from attr import fields
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from matplotlib.style import context
# Create your views here.
from .models import Task

class Tasklist(ListView):
    model=Task
    context_object_name='task'
class TaskDetail(DetailView):
    model=Task
    context_object_name='task'
class TaskCreate(CreateView):
    model='task'
    fields='__all__'
    success_url=reverse_lazy('task-list')

class TaskUpdate(UpdateView):
    model='task'

    fields='__all__'

    success_url=reverse_lazy('task-update')

class TaskDelete(DeleteView):
    model='task'
    fields='__all__'
    context_object_name='task'
    


