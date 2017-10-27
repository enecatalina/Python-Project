# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from datetime import datetime
from django.core.validators import RegexValidator
from django.core.files import File
from ..users_app.models import *
from ..property_details.models import *


class MessageManager(models.Manager):
    def create_validator(self, postData):
        errors = []
        if len(postData['content']) < 1:
            errors.append("content cannot be left blank!")
        if len(postData['content']) < 4:
            errors.append("Content should be more than 3 characters")
        if errors:
            return errors
        try:
            Message.objects.get(content=postData['content'])
            errors.append("Content already exists")
        except:
            pass
        return errors


class Message(models.Model):
    content = models.CharField(max_length=1000)
    sent_by = models.ForeignKey(User, related_name="sent_message", null = True)
    received_by = models.ForeignKey(User, related_name="received_by", null=True)
    about_listing = models.ForeignKey(listing, related_name="messaged_about", null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = MessageManager()
    def __unicode__(self):
         return str(self.sent_by, self.received_by)
    # def __unicode__(self):
    #     return unicode(self.sent_by, self.received_by, self.about_listing)

    # def __unicode__(self):
        # return "{0}, {1}".format(self.sent_by, self.received_by)
    # def __str__(self):
    #     return "content " + self.sent_by + self.received_by

    # def __repr__(self):
    #     return "<message object: {} {} {} {} {} {} {}>".format(self.id, self.content, self.sent_by, self.received_by, self.messaged_about, self.created_at, self.updated_at)
