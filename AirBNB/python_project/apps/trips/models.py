# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from datetime import datetime
from ..property_details.models import listing
from ..users_app.models import User
from datetime import timedelta

class TripsManager(models.Model):
    def booktripValidation(postData):
        is_valid = True
        errors = []
        if postData['guests'] < 0:
            errors.append('You can only have a positive number of guests')
        if postData['start_date']:
            errors.append('You need to fill out a start date')
        if postData['end_date']:
            errors.append('You need to fill out a start date')
        return (is_valid, errors)
        
class Trips(models.Model):
    start_date = models.DateTimeField(auto_now=False, auto_now_add=False)
    end_date = models.DateTimeField(auto_now=False, auto_now_add=False)
    # cancel  = models.CharField(max_length=255)
    pay = models.DecimalField(max_digits=6, decimal_places=2)
    listing = models.ForeignKey(listing, related_name="location")
    guests = models.ForeignKey(User, related_name="books")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = TripsManager()

