#coding=utf-8
from django.test import TestCase
from .models import *

class UserTestCase(TestCase):
    def setUp(self):
        User.objects.create_superuser(
            username='admort',
            email='me@admort.co'
        )
        User.objects.create(
            username='mikack',
            first_name='Mikasa',
            last_name='Ackerman',
            email='me@mikack.jp'
        )
        User.objects.create(
            username='erejae',
            first_name='Eren',
            last_name='Jaeger',
            email='me@erejae.jp'
        )