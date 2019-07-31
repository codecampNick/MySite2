from django.shortcuts import render

from .models import *


def index(request):
    employers = Company.objects.all().order_by('-start_date')
    accomplishments = Accomplishments.objects.all().order_by('rank')
    return render(request, 'employment_home.html',
                  {'title': 'Employment Home',
                   'employers': employers,
                   'accomplishments': accomplishments})

def aeriosdirect(request):
    return render(request, 'aerios-direct-inc.html',
                  {
                      'title': 'Aerios Direct Details',
                  })


def healthecareers(request):
    return render(request, 'health-ecareers.html',
                  {
                      'title': 'Health eCareers Details'
                  })


def diceholdings(request):
    return render(request, 'dice-holdings-inc.html',
                  {
                      'title': 'Dice Holdings Details'
                  })


def ontargetjobs(request):
    return render(request, 'ontargetjobs.html',
                  {
                      'title': 'Ontargetjobs Details',
                  })
