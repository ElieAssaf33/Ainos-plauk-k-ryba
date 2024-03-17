from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.core.mail import send_mail
from django.conf import settings
from .forms import RegistrationForm
from django.core.mail import send_mail

def index(request:HttpRequest):
    context = {}
    return render(request, 'kirpykla/index.html', context)

def services(request:HttpRequest):
    context = {}
    return render(request, 'kirpykla/services.html', context)

def contacts(request:HttpRequest):
    context = {}
    return render(request, 'kirpykla/contacts.html', context)

def register(request: HttpRequest):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        service = request.POST['service']
        email = request.POST['email']
        name = request.POST['name']
        date = request.POST['date']
        message = f'Labas {name}!, jūs užsiregistravote apsilankimui {date}, paslauga: {service}'
        send_mail(
        'Registracija',
        message,
        'settings.EMAIL_HOST_USER',
        [email],
        fail_silently=False
        )
    else:
        form = RegistrationForm()
    return render(request, 'kirpykla/register.html', {'form': form})
