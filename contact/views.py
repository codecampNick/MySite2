from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import ContactForm


def index(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid() and len(form.data['optional_contact']) == 0:
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message'] + '\n\ncontact via: ' + from_email
            try:
                send_mail(subject,message,'nick.jp.ross@gmail.com',['nick.jp.ross@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid Header Found')
            return HttpResponseRedirect('success')
    return render(request,'contact_home.html', {'title': 'Contact Home','form': form})


def successView(request):
    return render(request, 'success.html')
    #return HttpResponse('<hi>Your message is on its way!</h1>')