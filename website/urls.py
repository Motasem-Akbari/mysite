from django.urls import path
from website.views import *

urlpatterns = [
    path('', index_view),
    path('about-view', abuot_view),
    path('contect-view', contact_view)
]
