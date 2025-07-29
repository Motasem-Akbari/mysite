from django.urls import path
from website.views import *

app_name = 'website'

urlpatterns = [
    path('', index, name='home'),
    path('details', details, name='details'),
    path('profile', profile, name='profile'),
    path('browse', browse, name='browse'),
    path('streams', streams, name='streams')
]
