import email
from django.shortcuts import render
from django.conf import settings
from django.core.mail import send_mail
from django.http import HttpResponse
from django.contrib.auth.models import User




# Create your views here.
def register(request):
    if request.method=="POST":
        email = request.POST["email"]
        user = User.objects.create_user(
            email = email,
            username = email
            
        )
        send_mail(
            subject='A sexy subject',
            message='A horny message',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[user.email]
            )

    return render(request, 'register.html')
    
