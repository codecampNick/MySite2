from django.contrib import admin
from django.urls import path, include, re_path
# below depreciated in django 3.0
# from django.conf.urls import url
from . import views

urlpatterns = [
    re_path(r'^$', views.index),
    re_path(r'^success/?$', views.successView)
]