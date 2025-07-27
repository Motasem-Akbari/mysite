from django.shortcuts import render
from django.http import HttpResponse, JsonResponse


def index_view(request):
    return render(request,'website/index.html')


def abuot_view(request):
    return render(request, 'website/abuot.html')

def contact_view(request):
    return render(request, 'website/contact.html')
