from django.urls import path
from . import views

urlpatterns = [
    path('all_tasks/', views.TaskList.as_view(), name='task_list'),
    path('all_tasks/<slug:slug>/', views.CatList.as_view(), name='task_list'),

    path('task_detail/<slug:slug>', views.TaskDetail.as_view(), name='task_detail'),

]