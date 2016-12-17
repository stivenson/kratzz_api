#coding=utf-8
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import ugettext_lazy as _
from rest_framework.authtoken.admin import TokenAdmin

from .models import *


class UserAdmin(UserAdmin):

    fieldsets = (
        (_(u'user'), {'fields': ('username', 'password', 'email')}),
        (_(u'personal info'), {'fields': ('first_name', 'last_name', 'email')}),
        (_(u'permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
    )



TokenAdmin.raw_id_fields = ('user',)

admin.site.register(User, UserAdmin)