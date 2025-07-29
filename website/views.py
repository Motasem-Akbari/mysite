from django.shortcuts import render
from django.http import HttpResponse, JsonResponse


app_name = 'website'

def index(request):
    return render(request,'website/index.html')

def details(request):
    return render(request, 'website/details.html')

def profile(request):
    return render(request, 'website/profile.html')

def browse(request):
    return render(request,'website/browse.html')

def streams(request):
    return render(request,'website/streams.html')