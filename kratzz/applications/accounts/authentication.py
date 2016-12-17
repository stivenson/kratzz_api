import datetime
from datetime import timedelta
from django.conf import settings
from django.utils.timezone import pytz
from rest_framework.authentication import TokenAuthentication
from rest_framework import exceptions



class ExpiringTokenAuthentication(TokenAuthentication):
    def authenticate_credentials(self, key):
        ##print(self.model)
        try:
            token = self.model.objects.get(key=key)
        except self.model.DoesNotExist:
            raise exceptions.AuthenticationFailed('Invalid token')

        if not token.user.is_active:
            raise exceptions.AuthenticationFailed('User inactive or deleted')

        # This is required for the time comparison
        utc_now = datetime.utcnow()
        utc_now = utc_now.replace(tzinfo=pytz.utc)
        ##utc_now = datetime.datetime.utcnow().replace(tzinfo=utc)

        if token.created < utc_now - timedelta(seconds=1):
            raise exceptions.AuthenticationFailed('Token has expired')
        print('accounts :: authentication :: ExpiringTokenAuthentication \n Auth -> %s' %token.user)
        return token.user, token