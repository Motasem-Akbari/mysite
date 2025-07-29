from django.shortcuts import render
from django.http import HttpResponse, JsonResponse


def index(request):
    return render(request,'website/index.html')

def about(request):
    return render(request, 'website/about.html')

def contact(request):
    return render(request, 'website/contact.html')

def elements(request):
    return render(request, 'website/elements.html')

def packages(request):
    return render(request, 'website/packages.html')

def contact(request):
    return render(request, 'website/contact.html')
