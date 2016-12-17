#coding=utf-8
from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _

from rest_framework.authtoken.models import Token

from applications.core.helpers import *
from applications.core.models import *



class Contact(models.Model):
    """
    Stores contact information
    """
    photo = models.CharField(
        max_length=120,
        verbose_name=_('photo')
    )
    name_prefix = models.CharField(
        max_length=30,
        verbose_name=_('name prefix'),
        blank=True,
        null=True
    )
    first_name = models.CharField(
        max_length=15,
        verbose_name=_('first name')
    )
    middle_name = models.CharField(
        max_length=15,
        verbose_name=_('middle name'),
        blank=True,
        null=True
    )
    last_name = models.CharField(
        max_length=30,
        verbose_name=_('last name')
    )
    name_suffix = models.CharField(
        max_length=30,
        verbose_name=_('name suffix'),
        blank=True,
        null=True
    )
    nicknames = models.CharField(
        max_length=120,
        verbose_name=_('nicknames'),
        blank=True,
        null=True
    )
    birthday = models.DateField(
        verbose_name=_('birthday'),
        blank=True,
        null=True
    )
    notes = models.TextField(
        verbose_name=_('notes'),
        blank=True,
        null=True
    )

    class Meta:
        verbose_name = _(u'contact')

    def get_full_name(self):
        full_name = '{0}{1}{2}'.format(
            self.first_name,
            ' {3} '.format(self.middle_name) if self.middle_name else ' ',
            self.last_name
        )
        return full_name
