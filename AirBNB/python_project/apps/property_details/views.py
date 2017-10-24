# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from django.core.urlresolvers import reverse
from django.contrib import messages
from models import listing


# Create your views here.
def index(request):
    all_listings = listing.objects.all()
    for item in all_listings:
        print item.photo1
    context = {
        'listings': all_listings
    }
    return render(request, 'property_details/index.html', context)

def add(request):
    return render(request, 'property_details/new.html')

def create(request):
    errors = listing.objects.listing_validator(request.POST, request.FILES)
    if len(errors):
        for error in errors:
            print error
        return redirect(reverse('property:add'))
    else:
        return redirect(reverse('property:homepage'))

def display(request, listing_id):
    requested_listing = listing.objects.get(id=listing_id)
    print requested_listing.photo1
    context = {'requested_listing': requested_listing}
    return render(request, 'property_details/display.html', context)

def update(request, listing_id):
    return HttpResponse("this is the update page")

def destroy(request, listing_id):
    return HttpResponse("this is the destroy page")
