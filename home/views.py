from django.shortcuts import render
from django.views import View
from django.http import FileResponse, Http404, HttpResponse

# Create your views here
def index(request):
    return render(request, 'home/index.html')

def about(request):
    return render(request, 'home/about.html')

def services(request):
    return render(request, 'home/services.html')

def locations(request):
    return render(request, 'home/locations.html')

def forms(request):
    return render(request, 'home/forms.html')

def learn(request):
    return render(request, 'home/learn.html')

