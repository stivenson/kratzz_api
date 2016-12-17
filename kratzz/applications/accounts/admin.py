#coding=utf-8
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as UA
from django.utils.translation import ugettext_lazy as _
from rest_framework.authtoken.admin import TokenAdmin

from .models import *


class UserAdmin(UA):

    fieldsets = (
        (_(u'user'), {'fields': ('username', 'password', 'email')}),
        (_(u'permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
    )



TokenAdmin.raw_id_fields = ('user',)

admin.site.register(User, UserAdmin)