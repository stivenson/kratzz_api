#coding=utf-8
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from .models import *


class PhoneTypeAdmin(admin.ModelAdmin):

    fieldsets = (
        (_(u'phonetype'), {'fields': ('name',)}),
    )


class PhoneAdmin(admin.ModelAdmin):

        fieldsets = (
            (_(u'phone'), {'fields': ('country', 'number', 'contact', 'phone_type')}),
        )


admin.site.register(PhoneType, PhoneTypeAdmin)
admin.site.register(Phone, PhoneAdmin)
