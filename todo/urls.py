from django.urls import path
from . import views

urlpatterns = [
    path('all_tasks/', views.TaskList.as_view(), name='task_list'),
]