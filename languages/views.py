from django.shortcuts import render
from django.http.response import HttpResponse

def index(request):
    return render(request, 'languages_home.html')
