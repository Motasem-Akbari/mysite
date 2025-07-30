from django.shortcuts import render
from django.http import HttpResponse, JsonResponse


def blog(request):
    return render(request,'blog/blog.html')

def single_blog(request):
    return render(request, 'blog/single-blog.html')
