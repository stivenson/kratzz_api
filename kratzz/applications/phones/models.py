#coding=utf-8
from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _

from applications.core.helpers import *
from applications.core.models import *
from applications.contacts.models import *



class PhoneType(models.Model):
    """
    Stores contact information
    """
    name = models.CharField(
        max_length=30,
        verbose_name=_(u'name')
    )

    class Meta:
        verbose_name = _(u'phone type')

    def __str__(self):
        return self.name


class Phone(models.Model):
    """
    Stores contact information
    """
    country = models.CharField(
        max_length=2,
        verbose_name=_(u'country')
    )
    number = models.CharField(
        max_length=120,
        unique=True,
        verbose_name=_(u'photo')
    )
    contact = models.ForeignKey(
        Contact,
        verbose_name=_(u'contact'),
        related_name='phones',

    )
    phone_type = models.ForeignKey(
        PhoneType,
        verbose_name=_(u'phone type'),
        related_name='phones',

    )

    class Meta:
        verbose_name = _(u'phone')

    def __str__(self):
        return self.number