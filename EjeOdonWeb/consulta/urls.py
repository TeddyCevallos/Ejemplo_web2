from django.urls import path
from .views import *

urlpatterns = [
    path('',index, name='index'),
    path('portfolio/',portfolio, name='portfolio'),
    path('contact/',contact, name='contact'),    
]
