from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.paginator import Paginator
from .models import *

# Create your views here.
def index(request):
    return render(request, 'index.html')
def partners(request):
    return render(request, 'partners.html')
def auth(request):
    return render(request, 'auth.html')
def buildings(request):
    return render(request, 'buildings.html')
def materials(request):
    return render(request, 'materials.html')
def contracts(request):
    return render(request, 'contracts.html')
def permissions(request):
    return render(request, 'permissions.html')
def task_add(request):
    return render(request, 'task_add.html')


'''
Обработка формы
'''
def add_contract(request):
    if request.method == 'POST':
        # Получаем данные из формы
        contract_number = request.POST.get('contract_number')
        contract_date = request.POST.get('contract_date')
        partner = request.POST.get('partner')
        subject = request.POST.get('subject')

        # Создаём и сохраняем запись в БД
        Contract.objects.create(
            contract_number=contract_number,
            contract_date=contract_date,
            partner=partner,
            subject=subject,
        )
        
        return redirect('success_page')  # Редирект после успешного сохранения
    
    return render(request, 'contract_su.html')  # Отображаем форму
def success_page(request):
    return render(request, 'contract_su.html')

def contract_list(request):
    contracts = Contract.objects.all().order_by('-contract_date')
    
    paginator = Paginator(contracts, 3)  # Показывать по 10 договоров на странице
    page_number = request.GET.get('page')  # Получаем номер страницы из URL
    page_obj = paginator.get_page(page_number)  # Получаем нужную страницу

    return render(request, 'contracts.html', {'page_obj': page_obj})

##########################################################
def add_task(request):
    if request.method == 'POST':
        # Получаем данные из формы
        priority = request.POST.get('priority')
        deadline = request.POST.get('deadline')
        description = request.POST.get('description')
        title = request.POST.get('title')

        # Создаём и сохраняем запись в БД
        Taskadd.objects.create(
            title=title,
            deadline=deadline,
            description=description,
            priority=priority,
        )
        
        return redirect('success_page')  # Редирект после успешного сохранения
    
    return render(request, 'task_add.html')  # Отображаем форму

def task_list(request):
    task = Taskadd.objects.all().order_by('-deadline')
    
    paginator = Paginator(task, 3)  # Показывать по 10 договоров на странице
    page_number = request.GET.get('page')  # Получаем номер страницы из URL
    page_obji = paginator.get_page(page_number)  # Получаем нужную страницу

    return render(request, 'task_add.html', {'page_obji': page_obji})