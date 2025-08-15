from django.urls import path
from website.views import *

app_name= 'website'

urlpatterns = [
    path('', index,name='home'),
    path('about', about,name='about'),
    path('contact', contact,name='contact'),
    path('elements', elements,name='elements'),
    path('packages', packages,name='packages'),
    path('test', test_view,name='test'),

]
