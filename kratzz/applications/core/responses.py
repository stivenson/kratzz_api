#coding=utf-8

from rest_framework import status
from rest_framework.response import Response

from applications.constants import response_cons


def _default_response():
    data = {'message': ''}
    return Response(data, status.HTTP_200_OK)


def _response_404(name):
    data = {'message': response_cons.HTTP_404_NOT_FOUND.format(name)}
    return Response(data, status.HTTP_404_NOT_FOUND)


def _response_500():
    data = {'message': response_cons.HTTP_500_INTERNAL_SERVER_ERROR}
    return Response(data, status.HTTP_500_INTERNAL_SERVER_ERROR)


def short_response(value, name=None):
    response = _default_response()
    if status.HTTP_404_NOT_FOUND == value:
        response = _response_404(name)
    if status.HTTP_500_INTERNAL_SERVER_ERROR == value:
        response = _response_500()
    return response