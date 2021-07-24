from django.shortcuts import render, redirect
from .models import contactReport
from django.core.mail import EmailMessage
from django.conf import settings


def homeView(request):
    if request.method == 'POST':
        Name = request.POST.get('name')
        Email = request.POST.get('Email')
        Phone = request.POST.get('Phone')
        Subject = request.POST.get('Subject')
        Message = request.POST.get('Message')
        ct = contactReport(name=Name, email=Email, phone=Phone, subject=Subject, message=Message)
        ct.save()

        email_to_user = EmailMessage(Subject, Message, settings.EMAIL_HOST_USER, [Email,])
        email_to_admin = EmailMessage("I appreciate you contacting me. I or one of my colleagues will get back in touch with you soon!, Thnak you and Have a great day!", Email, [settings.EMAIL_HOST_USER,])
        email_to_user.send(fail_silently=True)
        email_to_admin.send(fail_silently=True)
        return redirect("home")
        
    return render(request, "home/index.html")
