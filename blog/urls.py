from django.urls import path
from blog.views import *

app_name= 'blog'

urlpatterns = [
    path('blog', blog,name='blog'),
    path('<int:pid>', single_blog,name='single-blog'),
    # path('post-<int:pid>', test,name='test'),
]
