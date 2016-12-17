#coding=utf-8
from __future__ import unicode_literals

from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.translation import ugettext_lazy as _

from rest_framework.authtoken.models import Token

from applications.core.helpers import *
from applications.core.models import *



class UserManager(BaseUserManager):

    def _create_user(self, username, email, password,
                     is_staff, is_superuser, **extra_fields):
        if not email:
            raise ValueError('Email is required')
        email = self.normalize_email(email)
        user = self.model(
            username=username,
            email=email,
            is_active=True,
            is_staff=is_staff,
            is_superuser=is_superuser,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, email, password=None, **extra_fields):
        return self._create_user(username, email, password, False, False, **extra_fields)

    def create_superuser(self, username, email, password=None, **extra_fields):
        return self._create_user(username, email, password, True, True, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    """
    Stores modified users for this particular system.
    """
    username = models.CharField(
        max_length=30,
        unique=True,
        verbose_name=_(u'username')
    )
    email = models.EmailField(
        max_length=60,
        unique=True,
        verbose_name=_(u'email')
    )

    objects = UserManager()

    is_active = models.BooleanField(
        default=True,
        verbose_name=_(u'is active')
    )
    is_staff = models.BooleanField(
        default=False,
        verbose_name=_(u'is staff')
    )

    USERNAME_FIELD = u'username'
    REQUIRED_FIELDS = [u'email']

    class Meta:
        verbose_name = _(u'user')

    def get_short_name(self):
        return '{0}'.format(self.username)


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)