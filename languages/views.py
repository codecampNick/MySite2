from django.shortcuts import render
from django.http.response import HttpResponse
from .models import *


def index(request):
    langs = Language.objects.all().order_by('-experience_level')
    star_value = {}
    for lang in langs:
        star_percent = (lang.experience_level / 5) * 100
        rounded = (round(star_percent / 10) * 10)
        if lang.name in star_value:
            continue
        else:
            star_value[lang.name] = rounded

    return render(request,'languages_home.html',
                  {
                      'title': 'Languages Home',
                      'langs': langs,
                      'star_value': star_value,
                  })
