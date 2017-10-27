# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.files import File
from django.db import models
from ..users_app.models import *


# Create your models here.
class listingManager(models.Manager):
    def listing_validator(self, postData, postFILES, current_user):
        errors = []
        #Check input information to see if it matches requirements
        if postData['user_title'] < 1:
            errors.append('Your house needs some kind of title')
        if postData['guests'] < 0:
            errors.append('You can only have a positive number of guests')
        if postData['beds'] < 0:
            errors.append('You can only have a positive number of beds')
        if postData['bathrooms'] < 0:
            errors.append('You can only have a positive number of bathrooms')
        if len(postData['country']) < 2:
            errors.append('You must enter a country')
        if len(postData['Street_one']) < 1:
            errors.append('You must enter an adress')
        if len(postData['city']) < 2:
            errors.append('You must enter a city')
        if len(postData['state'])< 2:
            errors.append('You must enter a city')
        if len(postData['zip']) < 5:
            errors.append('You must enter a zipcode')
        if postData['rate'] < 1: 
            errors.append('You must enter in a rate to charge')
        #If there are errors return the errors and stop this method
        if len(errors):
            return errors
        
        #Try grabbing an image if it was uploaded
        try:
            image = postFILES['image']
            print image
        except:
            image = ''
            print 'No image'

        #Get all the input information into variables
        user_title = postData['user_title']
        listing_type = postData['listing']
        property_type = postData['property_type']
        room_type = postData['type']
        dedicated_space = postData['space']
        guests = postData['guests']
        beds = postData['beds']
        bedtype = postData['bedtype']
        common_space = postData['common_space']
        bathrooms = postData['bathrooms']
        country = postData['country']
        Street_one = postData['Street_one']
        Street_two = postData['Street_two']
        city = postData['city']
        state = postData['state']
        zipcode = postData['zip']
        rate = postData['rate']
        selected_normal_amenities = postData.getlist('normal_amenities')
        selected_safety_amenities = postData.getlist('safety_amenities')
        selected_bonus_space = postData.getlist('bonus_space')
        user_description = postData['user_description']
        
        #create a new item/row in our listing table
        new_listing = listing.objects.create(
            title = user_title,
            listing_type = listing_type, 
            property_type = property_type, 
            room_type = room_type, 
            ded_space = dedicated_space, 
            guests = guests,
            beds = beds, 
            bedsize = bedtype, 
            common_space = common_space, 
            bathrooms = bathrooms, 
            Country = country, 
            street_one = Street_one,
            street_two = Street_two, 
            city = city, 
            state = state, 
            zip_code = zipcode, 
            photo1 = image, 
            rate = rate, 
            host_user_id=current_user,
            description=user_description)

        #create all the normal amenities
        for amenity in selected_normal_amenities:
            normal_amenities.objects.create(name = amenity, listing = new_listing)
        #create all the safety amenities
        for amenity in selected_safety_amenities:
            safety_amenities.objects.create(name = amenity, listing = new_listing)
        #create all the bonus spaces
        for space in selected_bonus_space:
            bonus_spaces.objects.create(name = space, listing = new_listing)

        #return an empty errors list signaling that the process was completed
        return errors


class listing(models.Model):
    title = models.CharField(max_length=20, default="Castle")
    listing_type = models.CharField(max_length = 15, default = 'Home')
    property_type = models.CharField(max_length = 15, default = 'Apartment')
    room_type = models.CharField(max_length = 15, default = 'Private room')
    ded_space = models.BooleanField()
    guests = models.IntegerField()
    beds = models.IntegerField()
    bedsize = models.CharField(max_length=15, null=True, blank=True)
    common_space = models.CharField(max_length=15, null=True, blank=True)
    bathrooms = models.IntegerField()
    Country = models.CharField(max_length = 100)
    street_one = models.CharField(max_length=200)
    street_two = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=20)
    zip_code = models.IntegerField()
    photo1 = models.ImageField(upload_to='uploads/%Y/%m', null=True, blank=True)
    photo2 = models.ImageField(upload_to='uploads/%Y/%m', null=True, blank=True)
    photo3 = models.ImageField(upload_to='uploads/%Y/%m', null=True, blank=True)
    photo4 = models.ImageField(upload_to='uploads/%Y/%m', null=True, blank=True)
    photo5 = models.ImageField(upload_to='uploads/%Y/%m', null=True, blank=True)
    photo6 = models.ImageField(upload_to='uploads/%Y/%m', null=True, blank=True)
    photo7 = models.ImageField(upload_to='uploads/%Y/%m', null=True, blank=True)
    photo8 = models.ImageField(upload_to='uploads/%Y/%m', null=True, blank=True)
    host_user = models.ForeignKey(User, related_name="host_listing", default=1)
    rate = models.FloatField()
    description = models.CharField(max_length = 1000 , null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = listingManager()

    def __str__(self):
        return "listing: " + self.host_user

class normal_amenities(models.Model):
    name = models.CharField(max_length=30)
    listing = models.ForeignKey(listing, related_name='normal_amenity')

class safety_amenities(models.Model):
    name = models.CharField(max_length=30)
    listing = models.ForeignKey(listing, related_name='safety_amenity')

class bonus_spaces(models.Model):
    name = models.CharField(max_length=30)
    listing = models.ForeignKey(listing, related_name='bonus_space')

class review(models.Model):
    content = models.CharField(max_length=1000)
    rating = models.IntegerField()
    location_id = models.ForeignKey(listing, related_name='received_ratings')
    rated_by = models.ForeignKey(User, related_name='ratings_given')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


