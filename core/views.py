# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse
from catalog.models import Category
from .forms import ContactForm
from django.core.mail import send_mail
from django.conf import settings
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.core.urlresolvers import reverse_lazy


User = get_user_model()

def index(request):
    return render(request,'index.html')

def contact(request):
    sucess = False
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            message = 'Nome: {0}\nE-mail:{1}\n{2}'.format(name,email,message)
            send_mail('Contato do Django E-Commerce',message,settings.DEFAULT_FROM_EMAIL,[settings.DEFAULT_FROM_EMAIL])
            sucess = True
    else:
        form = ContactForm()

    contexto = {
        'form': form,
        'sucess': sucess
    }
    return render(request,'contact.html', contexto)

def product(request):
    return render(request,'product.html')
