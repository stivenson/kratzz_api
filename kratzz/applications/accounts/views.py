#coding=utf-8
import datetime

from django.contrib.auth.models import Group
from django.http import HttpResponse, JsonResponse
from django.utils.timezone import utc
from django.utils.translation import ugettext_lazy as _
from django.views.decorators.csrf import csrf_exempt

from mail_templated import send_mail, EmailMessage
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, authentication_classes
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status, viewsets
from rest_framework import authentication, permissions

from applications.constants import *
from applications.core.helpers import *
from .models import *
from .forms import *
from .serializers import *



class ObtainExpiringAuthToken(ObtainAuthToken):
    """
    API endpoint that allows tokens to be obtained.
    ---
    """
    def post(self, request):
        """
        Somwthing here.
        """
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            token, created =  Token.objects.get_or_create(user=serializer.validated_data['user'])

            if not created:
                # update the created time of the token to keep it valid
                token.created = datetime.datetime.utcnow().replace(tzinfo=utc)
                token.save()

            # return Response({'token': token.key})
            response_data = {
                    'id': token.user.id,
                    'token': token.key
                }
            return Response(response_data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-last_login')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class JustForTestView(APIView):
    """
    View to test and play with fire.

    """
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAdminUser,)

    def get(self, request, format=None):
        data = {'email': constants.EmailConstant.ADRIAN_EMAIL.value[0]}
        return Response(data)


##@csrf_exempt
@authentication_classes(('rest_framework.authentication.TokenAuthentication',))
def user_fullname(request, pk):
    """
    API endpoint that allows the pk's user to retrieve its full name...
    This is just an example
    """
    try:
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return Response({}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        data = {'full_name': user.get_full_name}
        return JsonResponse(data)


obtain_expiring_auth_token = ObtainExpiringAuthToken.as_view()
just_for_test = JustForTestView.as_view()
