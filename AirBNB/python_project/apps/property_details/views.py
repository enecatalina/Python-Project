# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from django.core.urlresolvers import reverse
from django.contrib import messages
from models import listing, normal_amenities, safety_amenities, bonus_spaces, review
from ..users_app.models import *
from dummy import create_dummy_users, create_dummy_listings


# Create your views here.
def index(request):
    all_listings = listing.objects.all()
    if 'city' in request.session:
        search_listing = all_listings.filter(
            city=request.session['city'])
        # print search_listing.first().city
    else: 
        search_listing = listing.objects.all()
    context = {
        'listings_res': search_listing
    }
    # print context['listings_res']
    return render(request, 'property_details/index.html', context)

def listingResults(request):
    city = request.POST.get('user_search')
    request.session['city']= city 
    # print request.session['city']
    return redirect(reverse('property:homepage'))

def reset(request):
    del request.session['city']
    return redirect(reverse('property:homepage'))

def add(request):
    current_user = User.objects.get(id=request.session['user_id'])
    context = { 'user': current_user}
    return render(request, 'property_details/new.html', context)

def create(request):
    current_user = request.session['user_id']
    errors = listing.objects.listing_validator(request.POST, request.FILES, current_user)
    if len(errors):
        for error in errors:
            print error
        return redirect(reverse('property:add'))
    else:
        return redirect(reverse('property:homepage'))

def display(request, listing_id):
    requested_listing = listing.objects.get(id=listing_id)
    listing_normal_amenities = normal_amenities.objects.filter(listing = listing_id)
    listing_safety_amenities = safety_amenities.objects.filter(listing = listing_id)
    listing_bonus_space = bonus_spaces.objects.filter(listing = listing_id)
    try:
        listing_reviews = review.objects.filter(location_id = listing_id)
        review_count = len(listing_reviews)
    except:
        listing_reviews = ''
        review_count - 0
        pass
    context = {
        'requested_listing': requested_listing,
        'normal': listing_normal_amenities,
        'safety': listing_safety_amenities,
        'bonus': listing_bonus_space,
        'listing_reviews': listing_reviews,
        'review_count': review_count,
        }
    return render(request, 'property_details/display.html', context)

def create_review(request):
    review_content = request.POST['review']
    reviewed_listing = listing.objects.get(id = request.POST['listing_id']) 
    user_reviewing = User.objects.get(id = request.POST['user'])
    review_rating = request.POST['rating']
    review.objects.create(
        content = review_content,
        rating = review_rating,
        location_id = reviewed_listing,
        rated_by = user_reviewing
    )
    return redirect(reverse('property:display', args=request.POST['listing_id']))

def update(request, listing_id):
    return HttpResponse("this is the update page")

def destroy(request, listing_id):
    return HttpResponse("this is the destroy page")

def dummy(request):
    create_dummy_users()
    create_dummy_listings()
    return redirect('/')
