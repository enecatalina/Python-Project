# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from datetime import datetime
from django.core.validators import RegexValidator
from django.core.files import File
import re
import md5
import bcrypt
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
phone_regex = re.compile(r'^\+?1?\d{9,15}$')
# phone_regex = RegexValidator(
#     regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")



class UserManager(models.Manager):
    def register_validator(self, postData):
        errors = []
        if len(postData['first_name']) < 1:
            errors.append("Name cannot be empty!")
        if len(postData['last_name']) < 1:
            errors.append("Name cannot be empty!")
        if len(postData['first_name']) < 5 and postData['first_name'].isdigit():
            errors.append("Name cannot contain numbers")
        if len(postData['last_name']) < 5 and postData['last_name'].isdigit():
            errors.append("Name cannot contain numbers")
        if len(postData['email']) < 1:
            errors.append("Email cannot be blank!")
        elif not EMAIL_REGEX.match(postData['email']):
            errors.append("Invalid Email Address format!")
        if not phone_regex.match(postData['phone_number']):
            errors.append("Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
        if len(postData['password']) < 1:
            errors.append("Password should be more than 8 characters")
        if len(postData['confirm_password']) < 1:
            errors.append("Password should be more than 8 characters")
        if postData['password'] != postData['confirm_password']:
            errors.append("Confirm password and password do not match")
        if errors:
            return errors
        try:
            User.objects.get(email=postData['email'])
            errors.append("User already exists")
        except:
            pass
        return errors

    def login_validator(self, postData):
        errors = []
        if len(self.filter(email=postData['email'])) > 0:
            user = self.filter(email=postData['email'])[0]
            if bcrypt.checkpw(postData['password'].encode(), user.password.encode()):
                print ('yes, password!')
            else:
                errors.append("Invalid password")
        else:
            errors.append("No such user")
        if errors:
          return errors
        return user

class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    birthday = models.DateField(blank=True, default=datetime(2017, 01, 01))
    email = models.EmailField()
    password = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15, blank=True)
    gender_choices = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField(max_length=1, choices=gender_choices)
    language_choices = (
        ('EN', 'English'),
        ('SP', 'Spanish'),
        ('FR', 'French'),
        ('SW', 'Swahili'),
    )
    preferred_language = models.CharField(max_length=2, choices=language_choices, default='EN')
    currency_choices = (
        ('USD', 'United States'),
        ('AUD', 'Australia'),
        ('EUR', 'Euro'),
        ('GBP', 'Great Britain')
    )
    preferred_currency = models.CharField(max_length=3, choices=currency_choices, default='USD')
    location = models.TextField(max_length=200)
    user_description = models.TextField()
    profile_pic= models.ImageField(upload_to="profile_pics", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

    def __repr__(self):
        return "<user object: {} {} {} {} {} {} {} {} {} {} {} {} {} {}>".format(self.id, self.first_name, self.last_name, self.email,
         self.birthday, self.password, self.phone_number, self.gender, self.preferred_language, self.preferred_currency, self.location, 
         self.user_description, self.created_at, self.updated_at)


