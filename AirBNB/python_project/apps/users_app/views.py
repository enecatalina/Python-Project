# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, HttpResponse, redirect
from .models import User
from django.core.urlresolvers import reverse
from django.contrib import messages
import bcrypt

def home(request):
    return render(request, 'home.html')

def index(request):
    u = User.objects.all()
    context = {
        'users': u
    }
    return render(request, 'index.html', context)


def logme(request):
    u = User.objects.all()
    context = {
        'users': u
    }
    return render(request, 'logme.html', context)

def newhome(request):
    user = User.objects.get(id=request.session['user_id'])
    context = {
        'show_user': user
    }
    return render(request, "newhome.html", context)

def create(request):
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    birthday = request.POST['birthday']
    email = request.POST['email'].lower()
    password = request.POST['password']
    confirm_password = request.POST['confirm_password']
    phone_number = request.POST['phone_number']
    gender = request.POST['gender']
    print request.POST['preferred_language']
    preferred_language = request.POST['preferred_language']
    print request.POST['preferred_currency']
    preferred_currency = request.POST['preferred_currency']
    location = request.POST['location']
    user_description = request.POST['user_description']
    errors = User.objects.register_validator(request.POST)
    print errors
    if len(errors):
        for error in errors:
            messages.error(request, error)
        return redirect(reverse('users:index'))
    else:
        hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
        new_user = User.objects.create(
            first_name=first_name, last_name=last_name, birthday=birthday, email=email, password=hashed_password, phone_number=phone_number, 
            gender=gender, preferred_language=preferred_language, preferred_currency=preferred_currency, location=location, user_description=user_description)
        new_user.save()
        request.session['user_id'] = new_user.id
        return redirect(reverse('users:newhome'))


def login(request):
    email = request.POST['email'].lower()
    password = request.POST['password']
    errors = User.objects.login_validator(request.POST)
    if type(errors) == list:
        for error in errors:
            messages.error(request, error)
        return redirect(reverse('users:logme'))
    else:
        user = User.objects.get(email=request.POST['email'])
        request.session['user_id'] = user.id 
    return redirect(reverse('users:home'))


# def success_login(request):
#     user = User.objects.get(id=request.session['user_id'])
#     context = {
#         'show_user': user
#     }
#     return render(request, "newhome.html", context)

def edit(request, user_id):
    current_user = User.objects.get(id=request.session['user_id'])
    print current_user
    context = {
        'user_edit': current_user
    }
    return render(request, "edit.html", context)


def update(request, user_id):   #How to run validations thorugh an update?
    print user_id
    person = User.objects.get(id=user_id)
    person.first_name = request.POST.get('first_name', "")
    person.last_name = request.POST.get('last_name', "")
    person.email = request.POST.get('email', "")
    person.password = request.POST.get('password', "")
    person.phone_number = request.POST.get('phone_number', "")
    person.gender = request.POST.get('gender', "")
    person.preferred_language = request.POST.get('preferred_language', "")
    person.preferred_currency = request.POST.get('preferred_currency',  "")
    person.location = request.POST.get('location', "")
    person.user_description = request.POST.get('user_description', "")
    person.profile_pic = request.FILES.get('profile_pic', "")
    person.save()

    return redirect(reverse("users:view", args=(user_id)))

def view(request, user_id):
    current_user = User.objects.get(id=request.session['user_id'])
    print current_user
    context = {
        'user_profile': current_user
    }
    return render(request, "view.html", context)

def logout(request):
    request.session['user_id'] = None
    return redirect(reverse('users:index'))
