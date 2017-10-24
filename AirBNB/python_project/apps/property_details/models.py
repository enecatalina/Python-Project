# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.files import File
from django.db import models

# Create your models here.
class listingManager(models.Manager):
    def listing_validator(self, postData, postFILES):
        errors = []
        #Check input information to see if it matches requirements
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
        except:
            image = ''
            print 'No image'

        #Get all the input information into variables
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
        normal_amenities = postData.getlist('normal_amenities')
        safety_amenities = postData.getlist('safety_amenities')
        bonus_space = postData.getlist('bonus_space')
        
        #create a new item/row in our listing table
        listing.objects.create(
            listing_type = listing_type, 
            property_type = property_type, 
            room_type = room_type, 
            ded_space = dedicated_space, 
            guests = guests,
            beds = beds, 
            bedtype = bedtype, 
            com_space = common_space, 
            bathrooms = bathrooms, 
            Country = country, 
            street_one = Street_one,
            street_two = Street_two, 
            city = city, 
            state = state, 
            zip_code = zipcode, 
            normal_amenities = normal_amenities, 
            safety_amenities = safety_amenities, 
            bonus_spaces = bonus_space, 
            photo1 = image, 
            rate = rate )

        #return an empty errors list signaling that the process was completed
        return errors


class listing(models.Model):
    listing_choices = (
        ('Home', 'Home'),
        ('Hotel', 'Hotel'),
        ('Else', 'Something else'),
    )
    property_choices = (
        ('Apart', 'Apartment'),
        ('Condo', 'Condminium'),
        ('Guest', 'Guesthouse'),
        ('House', 'House'),
        ('Inlaw', 'In-law'),
        ('G_sui', 'Guest Suite'),
        ('Town', 'Townhouse'),
        ('Vaca', 'Vacation home'),
    )
    room_choices = (
        ('Entire', 'Entire place'),
        ('Priv', 'Private room'),
        ('Share', 'Shared room')
    )
    bed_choices = (
        ('Do', 'Double'),
        ('Qu', 'Queen'),
        ('Si', 'Single'),
        ('Ki', 'King'),
        ('So', 'Sofa bed'),
    )
    com_space_choices = (
        ('Co', 'Couch'),
        ('Fl', 'Floor matress'),
        ('So', 'Sofa bed'),
    )
    listing_type = models.CharField(max_length = 5, choices=listing_choices, default = 'Home')
    property_type = models.CharField(max_length = 5, choices= property_choices, default = 'Apart')
    room_type = models.CharField(max_length = 6, choices = room_choices, default = 'Priv')
    ded_space = models.BooleanField()
    guests = models.IntegerField()
    beds = models.IntegerField()
    bedtype = models.CharField(max_length = 2, choices = bed_choices, default = 'Do')
    com_space = models.CharField(max_length=2, choices=bed_choices, default='Do')
    bathrooms = models.IntegerField()
    Country = models.CharField(max_length = 100)
    street_one = models.CharField(max_length=200)
    street_two = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=20)
    zip_code = models.IntegerField()
    normal_amenities = models.TextField()
    safety_amenities = models.TextField()
    bonus_spaces = models.TextField()
    photo1 = models.ImageField(upload_to='uploads/%Y/%m', null=True, blank=True)
    photo2 = models.ImageField(upload_to='uploads/%Y/%m', null=True, blank=True)
    photo3 = models.ImageField(upload_to='uploads/%Y/%m', null=True, blank=True)
    photo4 = models.ImageField(upload_to='uploads/%Y/%m', null=True, blank=True)
    photo5 = models.ImageField(upload_to='uploads/%Y/%m', null=True, blank=True)
    photo6 = models.ImageField(upload_to='uploads/%Y/%m', null=True, blank=True)
    photo7 = models.ImageField(upload_to='uploads/%Y/%m', null=True, blank=True)
    photo8 = models.ImageField(upload_to='uploads/%Y/%m', null=True, blank=True)
    rate = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = listingManager()

    def __str__(self):
        return "listing: " + self.listing_type

#class review(models.model):
    #content = models.CharField(max_length=1000)
    #rating = models.IntegerField()
    # location_id = models.ForeignKey(listing, related_named='received_ratings')
    # rated_by = models.ForeignKey(user, related_name='ratings_given')
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)
