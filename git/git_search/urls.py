from django.conf.urls import include, url
from django.contrib import admin
from . import *

urlpatterns = [
     url(r'^index/', 'indexPage', name='index'),
]
