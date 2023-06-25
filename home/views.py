from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
from django.contrib import messages

from django.views.decorators.cache import never_cache

from django.contrib.auth.decorators import login_required
@login_required(login_url='login')
@never_cache
def home_page(request):
    return render(request, "home.html")

@login_required(login_url='login')
def about_page(request):
    return render(request, "about.html")
@login_required(login_url='login')
def services_page(request):
    return render(request, "services/services.html")

@login_required(login_url='login')
def contact_page(request):
    if request.method == 'POST':
        name = request.POST['w3lName']
        sender = request.POST['w3lSender']
        subject = request.POST['w3lSubject']
        message = request.POST['w3lMessage'] + f"\n\nFrom User: {name}\nUser Email: {sender}"

        send_mail(
            subject=subject,
            message=message,
            from_email=sender,
            recipient_list=["noorwebsite1@gmail.com"],
        )

        messages.success(
            request,
            "Thank you for your email. We will contact you as soon as possible."
        )

        return HttpResponseRedirect('/contact/')

    else:
        return render(request, "contact.html")