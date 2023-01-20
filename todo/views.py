from datetime import datetime, timezone

from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView, DetailView

from todo.models import Task
from todo.templatetags.time_until import calc_time


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

class Category(View):
    def get(self, request):
        # categories = Task.objects.values('category')
        # print(Task.objects.values('category'))
        all_categories = ['per', 'edu', 'spo', 'buy']
        with_data = []
        no_data = []
        for c in all_categories:
            if Task.objects.filter(category=c):
                with_data.append(c)
            else:
                no_data.append(c)

        context = {
            'with_data': with_data,
            'no_data': no_data
        }

        return render(request, 'todo/category.html', context=context)


class Manager(ListView):
    model = Task
    paginate_by = 5

    def get_queryset(self):
        return Task.objects.filter(due_date__lt=datetime.now(timezone.utc), done=False)
