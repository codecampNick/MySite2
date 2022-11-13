from django.urls import path, include, re_path
# below depreciated
# from django.conf.urls import url
from . import views

urlpatterns = [
    re_path(r'^$', views.index, name='employment_home'),
    re_path(r'aerios-direct-inc', views.aeriosdirect, name='about_aeriosdirect'),
    re_path(r'dice-holdings-inc/?', views.diceholdings, name='about_diceHoldings'),
    re_path(r'health-ecareers/?$', views.healthecareers, name='about_healthecareers'),
    re_path(r'ontargetjobs', views.ontargetjobs, name='ontargetjobs')
]