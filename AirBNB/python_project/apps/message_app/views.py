# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.shortcuts import render, HttpResponse, redirect
from .models import Message
from django.core.urlresolvers import reverse
from django.contrib import messages
from ..property_details.models import *
from ..users_app.models import *



def send(request, listing_id):
    current_user = User.objects.get(id=request.session['user_id'])
    current_listing = listing.objects.get(id=listing_id)
    print current_listing.id
    all_messages = Message.objects.all()
    sent_message = all_messages.filter(sent_by__in=[current_user])
    current_message = all_messages.filter(about_listing__in=[current_listing])
    print current_message
    context = {
          'listings': current_listing,
          'user_message' : sent_message,
          'message_profile': current_message,
    }
    return render(request, "messages.html", context)


def create(request, listing_id):
    content = request.POST['content']
    print content
    sent_by = request.POST['sent_by']
    print sent_by
    received_by = request.POST['received_by']
    print received_by
    about_listing = request.POST['about_listing']
    print about_listing
    errors = Message.objects.create_validator(request.POST)
    sent_by_user = User.objects.get(id=sent_by)
    received_by_user = User.objects.get(id=received_by)
    about_listing_id = listing.objects.filter(id=about_listing)
    print errors
    if len(errors):
        for error in errors:
            messages.error(request, error)
        return redirect(reverse('messages:send', args=(listing_id)))
    else:
        print sent_by_user
        print received_by_user
        new_message = Message.objects.create(content=content, sent_by=sent_by_user, received_by=received_by_user, about_listing=about_listing_id)
        new_message.save()
        request.session['message_id'] = new_message.id
        return redirect(reverse('messages:send', args=(listing_id)))

# def sendMessage(request, listing_id, message_id):
#     current_user = User.objects.get(id=request.session['user_id'])
#     current_listing = listing.objects.get(id=listing_id)
#     current_message = Message.objects.get(id=message_id)
#     messages = Message.objects.all()
#     current_message.about_listing.add(current_user)
#     current_message.save()

#     return redirect(reverse('messages:send', args=request.session['user_id']))

    
#  return redirect(reverse('messages:send', args=(user_id)))
