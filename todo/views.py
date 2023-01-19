from django.shortcuts import render
from django.views.generic import ListView, DetailView

from todo.models import Task


# Create your views here.
class TaskList(ListView):
    model = Task
    paginate_by = 5
    ordering = ['due_date']

class CatList(ListView):
    model = Task
    paginate_by = 5
    ordering = ['due_date']
class TaskDetail(DetailView):
    model = Task