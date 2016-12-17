#coding=utf-8
from django.conf.urls import url, include
from rest_framework import routers, serializers, viewsets

from .views import *

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)



urlpatterns = [
    #Obtain expiring auth token
    ###url(r'^auth/api-token$', obtain_expiring_auth_token),

    #url(r'^just-for-test/', views.just_for_test),
]