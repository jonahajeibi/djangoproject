from django.shortcuts import render
from django.http import HttpResponse
from .models import Companiess
from .models import Employees
# Create your views here.

def home(request):
    companiess = Companiess.objects.all()
    return render(request, 'index.html', {'companiess':companiess})


def employees(request):
    employees = Employees.objects.all()
    return render(request, 'employees.html', {'employees':employees})