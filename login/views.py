from django.shortcuts import render
from django.http import HttpResponse
from login.models import datalog
# Create your views here.

def home(request):
    return render(request, 'login/loginpage.html')

def dashboard(request):
    Datalog = datalog.objects.all()
    return render(request, 'login/dashboard.html', {'datalog':Datalog})
        

