from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return render(request, 'login/loginpage.html')

def dashboard(request):
    return render(request, 'login/dashboard.html')