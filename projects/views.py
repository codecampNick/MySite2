from django.shortcuts import render
from django.http import HttpResponse
from .models import *

def index(request):
    projects = Project.objects.all()
    return render(request, 'projects_home.html', {'title': "Projects Home", 'projects': projects})