#coding=utf-8
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from .models import *


class ContactAdmin(admin.ModelAdmin):

    fieldsets = (
        (_(u'contact'), {'fields': ('photo', 'name_prefix', 'first_name',
                                    'middle_name', 'last_name', 'name_suffix',
                                    'nicknames', 'birthday', 'notes')}),
    )


admin.site.register(Contact, ContactAdmin)
