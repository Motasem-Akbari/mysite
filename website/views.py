from django.shortcuts import render
from django.http import HttpResponse, JsonResponse


def index_view(request):
    return HttpResponse("<h1>Home page</h1>"
                        "(about-view)\n"
                        "(contect-view)")


def abuot_view(request):
    return HttpResponse("<h1>About page</h1>"
                        "(contect-view)")


def contact_view(request):
    return HttpResponse("<h1>Contact page</h1>"
                        "(abuot-view)")
