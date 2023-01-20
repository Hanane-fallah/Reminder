from django.shortcuts import render, redirect
from django.views import View
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

    def get_queryset(self):
        return Task.objects.filter(category=self.kwargs.get('slug'))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['slug'] = self.kwargs.get('slug')
        return context
    # queryset =


class TaskDetail(DetailView):
    model = Task

class Index(View):
    def get(self, request):
        return render(request, 'index.html')

    def post(self, request):

        title = self.request.POST['title']
        description = self.request.POST['desc']
        category = self.request.POST['category']
        priority = self.request.POST['priority']
        due_date = self.request.POST['due_date'] or None

        done = False
        if 'done' in self.request.POST.keys():
            done = True

        task = Task(title=title, description=description, category=category, priority=priority, due_date=due_date, done=done)
        task.save()

        return redirect('index')