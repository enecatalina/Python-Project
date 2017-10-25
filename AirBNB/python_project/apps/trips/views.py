# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from django.core.urlresolvers import reverse
from django.contrib import messages
from ..property_details.models import listing
from ..users_app.models import User
from ..trips.models import Trips
from datetime import date

# Create your views here.

def booking(request):
    all_listing = listing.objects.all()
    context = {
        'all_listing': all_listing
        }
    print all_listing
    return render(request, 'trips/booking.html', context)

def showlocation(request, listing_id):
    requested_listing = listing.objects.get(id=listing_id)
    print requested_listing.photo1
    context = {
        'requested_listing': requested_listing
        }
    return render(request, 'trips/show.html', context)

def bookatrip(request,listing_id):
    current_user = User.objects.get(id=request.session['user_id'])
    listing_id = listing.objects.get(id=listing_id)
    check = Trips.objects.bookatripValidation(request.POST)
    if check[0] == False:
        for error in check[1]:
            messages.add_message(request, messages.INFO, error, extra_tags="add_item")
            return redirect(reverse('trips:show'))
        else: 
            start_date = request.POST['start_date']
            end_date = request.POST['end_date']
            guests = request.POST['guests']
            listing = listing_id
            Trips.objects.create(start_date=start_date,end_date=end_date,guests=guests,listing=listing_id)
    print "booking was uploaded to datebase"
    return redirect('trips/show.html')

def mytrips(request):
    return render(request, 'trips/trips.html')