from django.shortcuts import render
from django.http import HttpResponse


def Home(request):
   return render(request, 'Home.html')


def index(request):
    return render(request, 'index.html')
def About(request):
    return render(request, 'About.html')
def Technology(request):
    return render(request, 'Technology.html')        


