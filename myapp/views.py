from django.shortcuts import render, redirect, HttpResponse
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.

def home(request):
    return render(request, 'index.html',context={})


def email(request): 
    subject = "This is our subject for the mail"
    message = "our email message"
    email_from = settings.EMAIL_HOST_USER    
    send_mail( subject, message, email_from, ['rahul.webllisto@gmail.com',] )
    return redirect('home')