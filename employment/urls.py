from django.urls import path, include
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='employment_home'),
    url(r'aerios-direct-inc', views.aeriosdirect, name='about_aeriosdirect'),
    url(r'dice-holdings-inc/?', views.diceholdings, name='about_diceHoldings'),
    url(r'health-ecareers/?$', views.healthecareers, name='about_healthecareers'),
    url(r'ontargetjobs', views.ontargetjobs, name='ontargetjobs')
]