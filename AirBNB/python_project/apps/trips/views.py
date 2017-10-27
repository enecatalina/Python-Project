# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from django.core.urlresolvers import reverse
from django.contrib import messages
from ..property_details.models import listing
from ..users_app.models import User
from ..trips.models import Trips
from datetime import datetime


# Create your views here.

def booking(request):
    all_listing = listing.objects.all()
    context = {
        'all_listing': all_listing
        }
    print all_listing
    return render(request, 'trips/booking.html', context)

def showlocation(request, listing_id):
    requested_listing = listing.objects.filter(id=listing_id)
    print requested_listing.photo1
    context = {
        'requested_listing': requested_listing
        }
    return render(request, 'trips/show.html', context)

def bookatrip(request,listing_id):
    if request.session['user_id'] == None:
        return redirect(reverse('users:index'))
    listing_id = listing.objects.get(id=listing_id)
    current_user = User.objects.get(id=request.session['user_id'])
    check = Trips.objects.bookatripValidation(request.POST)
    if check[0] == True:
        for error in check[1]:
            messages.add_message(request, messages.INFO, error, extra_tags="add_item")
            return redirect(reverse('property:homepage'))
        else: 
            current_user = User.objects.get(id=request.session['user_id'])
            start_date = request.POST['start_date']
            end_date = request.POST['end_date']
            guests = request.POST['guests']
            listing_id = listing_id
            pay = listing_id.rate 
            Trips.objects.create(start_date=start_date,end_date=end_date,guests=current_user,listing=listing_id,pay=pay)
            return redirect(reverse('trips:mytrips'))

def mytrips(request):
    user_id = User.objects.get(id=request.session['user_id'])
    mytrip = Trips.objects.filter(guests_id=user_id).order_by("start_date")
    trip = Trips.objects.get(id=1)
    start = trip.start_date.strftime('%Y %m %d')
    end = trip.end_date.strftime('%Y %m %d')
    mdate = trip.start_date.strftime('%Y-%m-%d')
    rdate = trip.end_date.strftime('%Y-%m-%d')
    print mdate
    print rdate
    mdate1 = datetime.strptime(mdate, "%Y-%m-%d").date()
    rdate1 = datetime.strptime(rdate, "%Y-%m-%d").date()
    delta =  (rdate1 - mdate1).days
    print delta
    myrate = trip.pay
    bill = delta * myrate
    print bill

    newArr=[]
    for trip in mytrip:
        start = trip.start_date.strftime('%Y-%m-%d')
        end = trip.end_date.strftime('%Y-%m-%d')
        mdate1 = datetime.strptime(start, "%Y-%m-%d").date()
        rdate1 = datetime.strptime(end, "%Y-%m-%d").date()
        delta =  (rdate1 - mdate1).days
        print delta
        myrate = trip.pay
        bill = delta * myrate
        this_trip = {'city': trip.listing.city, 'title': trip.listing.title, 'start': start, 'end': end, 'bill': bill}
        newArr.append(this_trip)

    print newArr
    context = {
        'mytrips': mytrip,
        'newarr': newArr
    }
    return render(request, 'trips/trips.html', context)
