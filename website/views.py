from django.shortcuts import render
from django.core.mail import send_mail


def home(request):
    return render(request,'home.html',{})

def privacy(request):
    return render(request,'privacy.html',{})

def aboutus(request):
    return render(request,'aboutus.html',{})

def contactus(request):
    return render(request,'contactus.html',{})

def clients(request):
    return render(request,'clients.html',{})

def services(request):
    return render(request,'services.html',{})