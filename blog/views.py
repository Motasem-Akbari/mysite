from django.shortcuts import render,get_object_or_404,redirect
from blog.models import Post,Comment
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from blog.forms import CommentForm
from django.contrib import messages
 


def blog(request,  **kwargs):
    posts = Post.objects.filter(status=1)
    if kwargs.get('cat_name') != None :
        posts = posts.filter(category__name = kwargs.get('cat_name'))
    if kwargs.get('author_username') != None:
        posts = posts.filter(author__username = kwargs.get('author_username'))
    if kwargs.get('tag_name') != None:
        posts = posts.filter(tags__name__in = [kwargs['tag_name']])
    
    posts = Paginator(posts, 3)
    try:
        page_number = request.GET.get('page')
        posts = posts.get_page(page_number)
    except PageNotAnInteger:
        posts = posts.get_page(1)
    except EmptyPage:
        posts = posts.get_page(1)
    context = {'posts': posts}
    return render(request, 'blog/blog.html', context)


# def blog(request, cat_name=None, author_username=None):                     #The second way
#     posts = Post.objects.filter(status=1)
    # if cat_name:
    #     posts = posts.filter(category__name = cat_name)
    # if author_username:
    #     posts = posts.filter(author__username = author_username)
    # if author_username:
    #     posts = posts.filter(author__username = author_username)


def single_blog(request,pid):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS,'your comment submitted successfully')
        else:
            messages.add_message(request,messages.ERROR,'your comment didnt submitted')
  
    posts = Post.objects.filter(status=1)
    post = get_object_or_404(posts,pk=pid)
    if not post.login_require:
        comments = Comment.objects.filter(post=post.id,approved=True).order_by("-created_date")
        form = CommentForm()
        context = {'post': post, 'comments':comments, 'form':form}
        return render(request, 'blog/single-blog.html',context)
    else:
        return redirect('accounts:login')

def blog_category(request,cat_name):
    posts = Post.objects.filter(status = 1)
    posts = posts.filter(category__name = cat_name)
    context = {'posts': posts}
    return render(request, 'blog/blog.html', context)

def blog_search(request):
    posts = Post.objects.filter(status=1)
    if request.method == "GET":
        # print(request.GET.get('s'))
        if s := request.GET.get('s'):
            posts = posts.filter(content__contains = s)
    context = {'posts': posts}
    return render(request, 'blog/blog.html', context)

# def test(request, pid):
#     # posts = Post.objects.all()
#     # context = {'posts': posts}
#     # context = {'name': name,'family_name':family_name,'age':age}
#     # context = {'pid': pid}
#     # post = Post.objects.get(id=pid)
#     post = get_object_or_404(Post,pk=pid)
#     context = {'post': post}

#     return render(request, 'blog/test.html', context)


def test(request):
    return render(request, 'blog/test.html')