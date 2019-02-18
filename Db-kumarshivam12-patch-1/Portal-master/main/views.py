from django.core.mail import send_mail

from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import ContactForm

def get_name(request):
    return render(request,template_name="name.html")