from django.shortcuts import render
from django.http.response import HttpResponse
from .models import *


def index(request):
    langs = Language.objects.all().order_by('-experience_level')
    return render(request, 'languages_home.html', {
        'title': "Languages Home",
        'langs': langs,
    })
