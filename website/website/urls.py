"""
URL configuration for website project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path
from app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",index,name= 'index'),
    path("partners/",partners,name= 'partners'),
    path("auth/",auth,name= 'auth'),
    path("buildings/",buildings,name= 'buildings'),
    path("materials/",materials,name= 'materials'),
    #path("contracts/",contracts,name='contracts'),
    path("permissions/",permissions,name='permissions'),
    path("task_add/",add_task,name='add_task'),
    path('add/', add_contract, name='add_contract'),
    path('success/', success_page, name='success_page'),
    path('task/', task_list, name='task_list'),
    path('contracts/', contract_list, name='contract_list'),
    
]
