from django.shortcuts import render,get_object_or_404
from blog.models import Post


def blog(request):
    posts = Post.objects.filter(status=1)
    context = {'posts': posts}
    return render(request, 'blog/blog.html', context)


def single_blog(request,pid):
    post = get_object_or_404(Post,pk=pid)
    context = {'post': post}
    return render(request, 'blog/single-blog.html',context)


def test(request, pid):
    # posts = Post.objects.all()
    # context = {'posts': posts}
    # context = {'name': name,'family_name':family_name,'age':age}
    # context = {'pid': pid}
    # post = Post.objects.get(id=pid)
    post = get_object_or_404(Post,pk=pid)
    context = {'post': post}

    return render(request, 'blog/test.html', context)
