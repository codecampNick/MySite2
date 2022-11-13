from django.urls import re_path
# below depreciated
# from django.conf.urls import url
from . import views


urlpatterns = [
    re_path(r'^$', views.index)
]