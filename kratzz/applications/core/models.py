#coding=utf-8
from __future__ import unicode_literals
from django.utils.translation import ugettext_lazy as _

from django.db import models



class TimeStampedModel(models.Model):
    """
    Abstract class to help models.
    """
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_(u'created at')
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name=_(u'updated at')
    )

    class Meta:
        abstract = True


class LocationModel(models.Model):
    """
    Abstract class to help models.
    """
    longitude = models.CharField(
        max_length=15,
        verbose_name=_(u'longitude')
    )
    latitude = models.CharField(
        max_length=15,
        verbose_name=_(u'latitude')
    )
    altitude = models.CharField(
        max_length=15,
        verbose_name=_(u'altitude')
    )

    class Meta:
        abstract = True