from django.urls import path
from blog.views import *
from blog.feeds import LatestPostsFeed


app_name= 'blog'

urlpatterns = [
    path('blog/', blog,name='blog'),
    path('<int:pid>', single_blog,name='single-blog'),
    path('category/<str:cat_name>', blog ,name='category'),
    path('tag/<str:tag_name>', blog ,name='tag'),
    path("author/<str:author_username>", blog , name="author"),
    path('search/',blog_search, name='search'),
    path('rss/feed', LatestPostsFeed(), name='post_feed'),
    # path('post-<int:pid>', test,name='test'),
    path('test', test,name='test'),
]
