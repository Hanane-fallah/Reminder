"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

from todo import views

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('', views.Index.as_view(), name='index'),
    path('category/', TemplateView.as_view(template_name='todo/category.html'), name='cat'),
    path('new_task/', TemplateView.as_view(template_name='todo/new_task.html'), name='new_task'),
    path('todo/', include(('todo.urls', 'todo'), namespace='todo'))
]
