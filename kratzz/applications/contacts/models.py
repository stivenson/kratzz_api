#coding=utf-8
from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _

from applications.core.helpers import *
from applications.core.models import *



class Contact(models.Model):
    """
    Stores contact information
    """
    photo = models.CharField(
        max_length=120,
        verbose_name=_(u'photo'),
        blank=True,
        null=True
    )
    name_prefix = models.CharField(
        max_length=30,
        verbose_name=_(u'name prefix'),
        blank=True,
        null=True
    )
    first_name = models.CharField(
        max_length=15,
        verbose_name=_(u'first name')
    )
    middle_name = models.CharField(
        max_length=15,
        verbose_name=_(u'middle name'),
        blank=True,
        null=True
    )
    last_name = models.CharField(
        max_length=30,
        verbose_name=_(u'last name')
    )
    name_suffix = models.CharField(
        max_length=30,
        verbose_name=_(u'name suffix'),
        blank=True,
        null=True
    )
    nicknames = models.CharField(
        max_length=120,
        verbose_name=_(u'nicknames'),
        blank=True,
        null=True
    )
    birthday = models.DateField(
        verbose_name=_(u'birthday'),
        blank=True,
        null=True
    )
    notes = models.TextField(
        verbose_name=_(u'notes'),
        blank=True,
        null=True
    )

    class Meta:
        verbose_name = _(u'contact')

    def __str__(self):
        return self.get_full_name()

    def get_full_name(self):
        full_name = '{0}{1}{2}'.format(
            self.first_name,
            ' {0} '.format(self.middle_name) if self.middle_name else ' ',
            self.last_name
        )
        return full_name
